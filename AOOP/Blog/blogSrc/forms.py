from django import forms
from blogSrc.models import Blog


class createBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
