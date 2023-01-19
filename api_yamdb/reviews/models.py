from django.db import models

from users.models import User
from .utils import ScoreChoice, validate_year

QUERY_SET_LENGTH = 15


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name[:QUERY_SET_LENGTH]


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name[:QUERY_SET_LENGTH]


class Title(models.Model):
    category = models.ForeignKey(
        Category,
        related_name='Titles',
        null=True,
        on_delete=models.SET_NULL,
    )
    genre = models.ManyToManyField(Genre, through='TitleGenre', )
    name = models.CharField(max_length=100)
    year = models.IntegerField(validators=[validate_year])
    description = models.TextField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name[:QUERY_SET_LENGTH]


class TitleGenre(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class Review(models.Model):
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews'
    )
    score = models.IntegerField(choices=ScoreChoice.choices(),
                                default=ScoreChoice.ONE)
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['author', 'title'],
                                    name='unique_review')
        ]


class Comment(models.Model):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)
