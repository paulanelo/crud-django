from django.urls import path

from .views import HomePage, CreatePost, EditPost, DeletePost

urlpatterns = [
  path('', HomePage.as_view(), name='home'),
  path('post/', CreatePost.as_view(), name='add_post'),
  path('edit/<pk>/', EditPost.as_view(), name='edit_post'),
  path('delete/<pk>/', DeletePost.as_view(), name='delete_post')
]