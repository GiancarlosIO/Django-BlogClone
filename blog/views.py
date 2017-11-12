# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
# reverse lazy only run when the method is called
from django.urls import reverse, reverse_lazy
# if you want to use class-based-view you need to use mixins
from django.contrib.auth.mixins import LoginRequiredMixin
# login decorator for func-bases-view
from django.contrib.auth.decorators import login_required
# CRUD views
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
# get_object_or_404 try to find a record, if it not exists return a 404 status code
from django.shortcuts import render, get_object_or_404, redirect

# models
from .models import Comment, Post

# forms
from .forms import PostForm, CommentForm

# Create your views here.
class AboutView(TemplateView):
    template_name = 'blog/about.html'

##################################
# POST VIEWS
##################################
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(published_at__lte=timezone.now()).order_by('-published_at')

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('blog:post_list')
    context_object_name = 'post'
    model = Post

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login'
    redirect_field_name = 'blog/post_list.html'

    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_at__isnull=True).order_by('-created_at')

## PUBLISH THE POST

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()

    return redirect('blog:post_detail', pk=pk)

##################################
# COMMENT LIST
##################################

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = CommentForm()
        context = {
            'form': form,
        }

    return render(request, 'blog/comment_form.html', context=context)

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()

    return redirect('blog:post_detail', pk=comment.post.pk)

@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()

    return redirect('blog:post_detail', pk=post_pk)