from django import forms
from .models import Blog

class EditBlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=('title','content')
        