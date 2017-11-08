# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.views.generic import TemplateView, ListView
from django.shortcuts import render

from .models import Comment, Post

# Create your views here.
class AboutView(TemplateView):
    template_name = 'blog/about.html'

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

