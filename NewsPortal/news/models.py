from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        post_ratings_sum = self.post_set.aggregate(Sum('rating'))['rating__sum'] * 3 if self.post_set.exists() else 0

        # Получить общий рейтинг всех комментариев, автор которых данный автор
        author_comment_ratings_sum = Comment.objects.filter(post__author=self).aggregate(Sum('rating'))[
            'rating__sum'] if Comment.objects.filter(post__author=self).exists() else 0

        # Получить рейтинг всех комментариев к статьям данного автора
        post_comment_ratings_sum = Comment.objects.filter(post__author__user=self.user).aggregate(Sum('rating'))[
            'rating__sum'] if Comment.objects.filter(post__author__user=self.user).exists() else 0

        self.rating = post_ratings_sum + author_comment_ratings_sum + post_comment_ratings_sum
        self.save()


class Category(models.Model):
    category = models.CharField(unique=True, max_length=255)


class Post(models.Model):
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    is_news = models.BooleanField(default=True)     # False - статья
    post_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[:124] + '...'

    # def __str__(self):
    #     # заголовок, дата публикации в формате день.месяц.год, затем первые 20 слов текста статьи
    #     return f'{self.title} ({self.post_date.strftime("%d.%m.%Y")}): {" ".join(self.text.split()[:20])}...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
