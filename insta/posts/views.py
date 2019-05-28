from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm, EditForm

class HomePage(ListView):
  model = Post
  template_name = 'index.html'

class CreatePost(CreateView):
  model = Post
  form_class = PostForm
  template_name = 'post.html'
  success_url= reverse_lazy('home')

class EditPost(UpdateView):
  model = Post
  form_class = EditForm
  template_name = 'edit.html'
  success_url = reverse_lazy('home')

class DeletePost(DeleteView):
  model = Post
  template_name = 'delete.html'
  success_url = reverse_lazy('home')