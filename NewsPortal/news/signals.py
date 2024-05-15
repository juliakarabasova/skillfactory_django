from django.db.models.signals import m2m_changed
from django.dispatch import receiver  # импортируем нужный декоратор
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .models import Post, PostCategory


# в декоратор передаётся первым аргументом сигнал, на который будет реагировать эта функция,
# и в отправители надо передать также модель
@receiver(m2m_changed, sender=Post.categories.through)
def notify_subscribers(sender, instance, **kwargs):

    if kwargs['action'] != 'post_add':
        return

    html_content = render_to_string(
        'new_post.html',
        {
            'post': instance,
        }
    )
    text_content = strip_tags(html_content)

    for cat in PostCategory.objects.filter(post_id=instance.pk):

        msg = EmailMultiAlternatives(
            subject=f'Новая запись в категории {cat.category}',
            body=text_content,
            from_email='juliakarabasova@yandex.ru',
            # recipient_list=Category.objects.get(pk=instance.category.pk).subscribers.all()
            to=cat.category.subscribers.all().values_list('email', flat=True)
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()  # отсылаем
