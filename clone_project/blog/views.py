from django.shortcuts import render
from blog.models import Post,Comment
from blog.forms import PostForm,CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import (TemplateView,DetailView,CreateView,UpdateView,
                                    DeleteView,ListVeiw)
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListVeiw):
    template_name = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post 

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = '/blog/post_details.html'
    form_class = PostForm
    model = Post 

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = '/blog/post_details.html'
    form_class = PostForm
    model = Post 

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListVeiw):
    login_url = '/login/'
    redirect_field_name = '/blog/post_details.html'
    model = Post 

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-published_date')