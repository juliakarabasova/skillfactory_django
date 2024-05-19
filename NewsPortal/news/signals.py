from django.db.models.signals import m2m_changed
from django.dispatch import receiver  # импортируем нужный декоратор

from .models import Post
from .tasks import notifier


# в декоратор передаётся первым аргументом сигнал, на который будет реагировать эта функция,
# и в отправители надо передать также модель
@receiver(m2m_changed, sender=Post.categories.through)
def notify_subscribers(sender, instance, **kwargs):

    if kwargs['action'] != 'post_add':
        return

    notifier.delay(instance.pk)

    # html_content = render_to_string(
    #     'new_post.html',
    #     {
    #         'post': instance,
    #     }
    # )
    # text_content = strip_tags(html_content)
    #
    # for cat in PostCategory.objects.filter(post_id=instance.pk):
    #
    #     msg = EmailMultiAlternatives(
    #         subject=f'Новая запись в категории {cat.category}',
    #         body=text_content,
    #         from_email='Skillfactory NewsPortal <juliakarabasova@yandex.ru>',
    #         # recipient_list=Category.objects.get(pk=instance.category.pk).subscribers.all()
    #         to=cat.category.subscribers.all().values_list('email', flat=True)
    #     )
    #     msg.attach_alternative(html_content, "text/html")
    #     msg.send()  # отсылаем
