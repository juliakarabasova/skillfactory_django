from django.urls import path
from .views import (NewsList, NewsDetail, NewsFilter, NewsCreate, NewsUpdate, NewsDelete, CategoryList,
                    subscribe, unsubscribe)

urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),
    path('<int:pk>', NewsDetail.as_view()),
    path('search', NewsFilter.as_view(), name='news_filter'),
    path('create', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('categories/', CategoryList.as_view(), name='categories'),
    path('categories/<int:pk>/subscribe/', subscribe, name='subscribe'),
    path('categories/<int:pk>/unsubscribe/', unsubscribe, name='unsubscribe'),
]
