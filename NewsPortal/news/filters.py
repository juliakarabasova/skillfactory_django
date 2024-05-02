from django.forms import DateInput
from django_filters import FilterSet, DateFilter, CharFilter
from .models import Post


class PostFilter(FilterSet):
    post_date = DateFilter(widget=DateInput(attrs={'type': 'date'}), lookup_expr='gt',
                           field_name='post_date', label='Дата публикации позднее')
    title = CharFilter(lookup_expr='icontains', field_name='title', label='Заголовок')
    author = CharFilter(lookup_expr='icontains', field_name='author__user__username', label='Имя автора')

    class Meta:
        model = Post
        fields = ['title', 'author', 'post_date']
