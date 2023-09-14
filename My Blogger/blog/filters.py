import django_filters
from .models import Blog

class BlogFilter(django_filters.FilterSet):
    # author = django_filters.CharFilter(field_name='author',lookup_expr='icontains')
    # title = django_filters.CharFilter(field_name='title',lookup_expr='icontains')
    description = django_filters.CharFilter(field_name='description',lookup_expr='icontains',label='Search')
    # category = django_filters.CharFilter(field_name='category',lookup_expr='icontains')
    
    class Meta:
        model = Blog
        fields = [
            'description',
        ]
        