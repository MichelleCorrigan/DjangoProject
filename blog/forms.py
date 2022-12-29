from .models import Comment, Post
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'content', 'featured_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control-l'}),
            'author': forms.TextInput(attrs={'class': 'form-control-l', 'value': '', 'id': 'creator', 'type': 'hidden'}),  # noqa
            'content': SummernoteWidget(),
            'featured_image': forms.FileInput(attrs={'class': 'form-control-m'}),  # noqa
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'featured_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control-l'}),
            'author': forms.Select(attrs={'class': 'form-control-sm'}),
            'content': SummernoteWidget(),
            'featured_image': forms.FileInput(attrs={'class': 'form-control-m'}),  # noqa
        }
