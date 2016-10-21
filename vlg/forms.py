__author__ = 'Kona'
from django import forms
from django.forms import ModelForm, HiddenInput, widgets
from vlg.models import Post,Comment


class newPostForm(ModelForm):
    class Meta:
        model = Post
        fields=['title', 'slug', 'text']

class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=['text']
        #widgets={
        #    'user':HiddenInput(),
        #    'post':HiddenInput(),
        #}