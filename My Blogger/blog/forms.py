from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class  Meta:
        model = Comment
        fields = ['first_name','last_name','email','text']
        verbose_name = 'Add Comment'
        verbose_name_plural = 'Add Comments'