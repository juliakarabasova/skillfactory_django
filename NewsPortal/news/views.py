from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Post, Author, User, PostCategory
from .filters import PostFilter
from .forms import NewsForm


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
