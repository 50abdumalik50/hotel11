from django import forms

from apps.news.models import Post, PostImage, Comment


class PostImagesForm(forms.ModelForm):
    class Meta:
        models = PostImage
        fields = ['image',]
        widgets = {'image': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
        })}


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'description',
                  ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
        ]