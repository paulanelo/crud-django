from django import forms
from .models import Post

class PostForm(forms.ModelForm):
  
  class Meta:
    model = Post
    fields = ['legend', 'photo']
    labels = {
      'legend': ('Legenda'),
      'photo': ('Foto')
    }
    widgets = {
      'legend': forms.TextInput(attrs={'class': 'form-control'})
    }

class EditForm(forms.ModelForm):

  class Meta:
    model = Post
    fields = ['legend']
    labels = {
      'legend': ('Legenda')
    }
    widgets = {
      'legend': forms.TextInput(attrs={'class': 'form-control'})
    }