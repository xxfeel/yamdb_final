from rest_framework import serializers

from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User


class CategorySerializer(serializers.ModelSerializer):
    '''Сериализатор для категорий.'''

    class Meta:
        fields = ('name', 'slug')
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    '''Сериализатор для жанров.'''

    class Meta:
        fields = ('name', 'slug')
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    '''Сериализатор для произведений.'''
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(read_only=True, many=True)
    rating = serializers.IntegerField()

    class Meta:
        fields = (
            'id', 'name', 'year', 'rating', 'description', 'genre', 'category'
        )
        model = Title


class TitleCreateSerializer(serializers.ModelSerializer):
    '''Сериализатор для создания произведений.'''
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True,
    )

    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all(),
    )

    class Meta:
        model = Title
        fields = (
            'id', 'name', 'year', 'description', 'genre', 'category'
        )


class UserSerializer(serializers.ModelSerializer):
    """Cоздание пользователя администратором."""
    role = serializers.ChoiceField(
        choices=User.USER_ROLE_CHOICES,
        default=User.USER
    )

    class Meta:
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role',
        )
        model = User

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Даже администраторам запрещено использовать имя me '
                'в качестве username при создании пользователей.'
            )
        return value


class ProfileEditSerializer(serializers.ModelSerializer):
    """Редактирование профиля."""
    class Meta:
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role',
        )
        model = User
        read_only_fields = ('role',)

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Использовать имя me в качестве username запрещено.'
            )
        return value


class RegistrationSerializer(serializers.ModelSerializer):
    """Регистрация пользователя."""
    role = serializers.HiddenField(default='user')

    class Meta:
        fields = ('username', 'email', 'role')
        model = User

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Использовать имя me в качестве username запрещено.'
            )
        return value


class GetTokenSerializer(serializers.ModelSerializer):
    """Получение токена."""
    confirmation_code = serializers.CharField()
    username = serializers.CharField()

    class Meta:
        fields = ('username', 'confirmation_code',)
        model = User


class ReviewSerializer(serializers.ModelSerializer):
    '''Сериализатор для отзывов к произведениям.'''
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True,
    )

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')

    def validate(self, data):
        if self.context['request'].method == 'PATCH':
            return data
        author = self.context.get('request').user
        title = self.context['view'].kwargs.get('title_id')
        if author.reviews.filter(title=title).exists():
            raise serializers.ValidationError(
                'You cannot make a review twice')
        return data


class CommentSerializer(serializers.ModelSerializer):
    '''Сериализатор для комментариев к отзывам.'''
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    review = serializers.HiddenField(default='review')

    class Meta:
        fields = ('id', 'review', 'text', 'author', 'pub_date')
        model = Comment
