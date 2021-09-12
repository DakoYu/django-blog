from django.db import models
from django.shortcuts import render
from django.views.generic.detail import DetailView
from blog.models import Post
from blog.forms import PostForm
from django.utils import timezone
from django.views.generic import TemplateView, ListView, CreateView

# Create your views here.
class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class PostCreateView(CreateView):
    form_class = PostForm
    model = Post

class AboutView(TemplateView):
    template_name = 'about.html'

