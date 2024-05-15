from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .models import Post, Author, User, PostCategory, Category
from .filters import PostFilter
from .forms import NewsForm, SubscribeForm


class NewsList(ListView):
    model = Post
    ordering = '-post_date'
    # queryset = Product.objects[.filter(price__lt=300)].order_by(-name)

    template_name = 'news.html'
    context_object_name = 'news'

    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        for post in queryset:
            post.text_categories = ', '.join(
                list(PostCategory.objects.filter(post=post).values_list('category__category', flat=True))
            )
        return queryset


class NewsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class NewsFilter(ListView):
    model = Post
    ordering = '-post_date'

    template_name = 'news_search.html'
    context_object_name = 'news'

    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        self.filterset = PostFilter(self.request.GET, queryset)

        for post in self.filterset.qs:
            post.text_categories = ', '.join(
                list(PostCategory.objects.filter(post=post).values_list('category__category', flat=True))
            )

        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)

    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'
    success_url = reverse_lazy('news_list')

    def form_valid(self, form):
        post = form.save(commit=False)

        # author_name = form.cleaned_data['author_name']
        #
        # new_user, created = User.objects.get_or_create(username=author_name)
        # author, created = Author.objects.get_or_create(user=new_user)
        #
        # post.author = author
        post.is_news = True
        post.save()

        # отправляем письмо
        # send_mail(
        #     subject=f'New post: {post.title}',
        #     # имя клиента и дата записи будут в теме для удобства
        #     message=post.text,  # сообщение с кратким описанием проблемы
        #     from_email='juliakarabasova@yandex.ru',  # здесь указываете почту, с которой будете отправлять (об этом попозже)
        #     recipient_list=['YuliaK2001@yandex.ru', 'yulia.kara14@gmail.com']  # здесь список получателей. Например, секретарь, сам врач и т. д.
        # )

        return super().form_valid(form)


class ArticleCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)

    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'
    success_url = reverse_lazy('news_list')

    def form_valid(self, form):
        post = form.save(commit=False)

        # author_name = form.cleaned_data['author_name']
        #
        # new_user, created = User.objects.get_or_create(username=author_name)
        # author, created = Author.objects.get_or_create(user=new_user)
        #
        # post.author = author
        post.is_news = False
        post.save()

        return super().form_valid(form)


class NewsUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)

    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'
    success_url = reverse_lazy('news_list')


class NewsDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)

    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')


class SubscribeView(LoginRequiredMixin, FormView):
    form_class = SubscribeForm
    template_name = 'subscribe.html'
    success_url = reverse_lazy('subscribe_success')

    def form_valid(self, form):
        # category = form.cleaned_data['category']
        category = form.save(commit=False)

        # Check if user is already subscribed to the selected category
        if category.subscribers.filter(id=self.request.user.id).exists():
            messages.warning(self.request, 'Вы уже подписаны на эту категорию.')
            return redirect(self.success_url)

        # Add user to subscribers
        category.subscribers.add(self.request.user)
        category.save()

        return super().form_valid(form)


def subscribe_success(request):
    category_name = request.GET.get('category')  # Or request.POST.get('category') depending on how you pass it

    return render(request, 'subscribe_success.html', {'category_name': category_name})


class CategoryList(ListView):
    model = Category
    template_name = 'categories.html'
    context_object_name = 'categories'


@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)
    return redirect('categories')


@login_required
def unsubscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.remove(user)
    return redirect('categories')
