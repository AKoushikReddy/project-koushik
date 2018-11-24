from django import forms
from .models import Post


# Form for Post Model, which can only be accessed from admin app.

class HomeForm(forms.ModelForm):
    post = forms.CharField(required=True)

    class Meta:
        model = Post
        fields = ('post',)
