from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


class AddPost(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'content', 'url']
