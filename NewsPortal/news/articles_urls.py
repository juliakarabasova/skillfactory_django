from django.urls import path
from .views import ArticleCreate, NewsUpdate, NewsDelete

urlpatterns = [
    path('create', ArticleCreate.as_view(), name='article_create'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='article_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='article_delete'),
]
