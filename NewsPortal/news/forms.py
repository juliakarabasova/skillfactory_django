from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class NewsForm(forms.ModelForm):
    # author_name = forms.CharField(min_length=10, max_length=100)
    # title = forms.CharField(min_length=10, max_length=255)
    # text = forms.CharField(min_length=10, widget=forms.Textarea)
    # categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'text',
            'categories',
        ]
        labels = {
            'author': 'Автор',
            'title': 'Заголовок',
            'text': 'Текст',
            'categories': 'Категории'
        }

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        self.fields['author'].empty_label = 'Без автора'

        # try:
        #     self.fields['author_name'].initial = self.instance.author.user.username
        # except AttributeError:
        #     pass

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("text")

        name = cleaned_data.get("title")
        if name == description:
            raise ValidationError(
                "Текст не должен быть идентичным заголовку."
            )

        return cleaned_data
