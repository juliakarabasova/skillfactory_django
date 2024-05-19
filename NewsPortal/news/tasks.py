from celery import shared_task

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.db.models import Q
from django.utils import timezone

from datetime import datetime, timedelta

from .models import Post, PostCategory, Category


@shared_task
def notifier(instance_key):
    instance = Post.objects.get(pk=instance_key)

    html_content = render_to_string(
        'new_post.html',
        {
            'post': instance,
        }
    )
    text_content = strip_tags(html_content)

    for cat in PostCategory.objects.filter(post_id=instance_key):
        msg = EmailMultiAlternatives(
            subject=f'Новая запись в категории {cat.category}',
            body=text_content,
            from_email='Skillfactory NewsPortal <juliakarabasova@yandex.ru>',
            # recipient_list=Category.objects.get(pk=instance.category.pk).subscribers.all()
            to=cat.category.subscribers.all().values_list('email', flat=True)
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()  # отсылаем


@shared_task
def weekly_update():
    end_date = timezone.now()
    start_date = end_date - timedelta(days=7)

    for category in Category.objects.all():
        posts_last_week = Post.objects.filter(
            Q(categories=category) & Q(post_date__gte=start_date, post_date__lte=end_date)
        )

        if not posts_last_week:
            continue

        subject = f'Обновления в категории "{category.category}" за неделю'

        html_content = render_to_string(
            'weekly_update.html',
            {
                'category': category.category,
                'news': posts_last_week,
            }
        )

        text_content = strip_tags(html_content)

        msg = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email='Skillfactory NewsPortal <juliakarabasova@yandex.ru>',
            to=category.subscribers.all().values_list('email', flat=True)
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
