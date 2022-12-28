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
        fields = ('title', 'slug', 'author', 'content', 'featured_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control-l'}),
            'slug': forms.TextInput(attrs={'class': 'form-control-l'}),
            'author': forms.Select(attrs={'class': 'form-control-sm'}),
            'content': SummernoteWidget(),
            'featured_image': forms.FileInput(attrs={'class': 'form-control-m'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'featured_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control-l'}),
            # 'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control-sm'}),
            'content': SummernoteWidget(),
            'featured_image': forms.FileInput(attrs={'class': 'form-control-m'}),
        }
