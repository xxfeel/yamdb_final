from django_filters import rest_framework as filter

from reviews.models import Title


class TitleFilter(filter.FilterSet):
    '''Фильтры для произведений.'''
    category = filter.CharFilter(field_name='category__slug',)
    genre = filter.CharFilter(field_name='genre__slug',)
    name = filter.CharFilter(field_name='name', lookup_expr='contains')
    year = filter.NumberFilter(field_name='year',)

    class Meta:
        model = Title
        fields = ['category', 'genre', 'name', 'year']
