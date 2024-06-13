from django import forms
from .models import Post, Comment, Blog


class BlogCreationForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name']
        widget = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class BlogEditForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name']
        widget = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class CommentCreationForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widget = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentEditForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widget = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
