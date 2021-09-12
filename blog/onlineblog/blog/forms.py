from django import forms
from django.forms import widgets
from blog.models import Post

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
                    'author':forms.TextInput(attrs={'class':'form-control'}),
                    'title':forms.TextInput(attrs={'class':'form-control'}),
                    'text':forms.Textarea(attrs={'class':'form-control'})
        }