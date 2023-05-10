from .models import Comment, Post, Category
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'content', 'featured_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control-l'}),
            'author': forms.TextInput(attrs={'class': 'form-control-l', 'value': '', 'id': 'creator', 'type': 'hidden'}),  # noqa
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control-l'}),  # noqa
            'content': SummernoteWidget(),
            'featured_image': forms.FileInput(attrs={'class': 'form-control-m'}),  # noqa
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'content', 'featured_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control-l'}),
            'author': forms.Select(attrs={'class': 'form-control-sm'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control-l'}),  # noqa
            'content': SummernoteWidget(),
            'featured_image': forms.FileInput(attrs={'class': 'form-control-m'}),  # noqa
        }
