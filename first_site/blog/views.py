from django.shortcuts import render
from django.views import generic

from .models import Post


class ListView(generic.ListView):
    template_name = 'blog/blog.html'

    def get_queryset(self):
        """Return the last 25 blog post titles"""
        return Post.objects.order_by('-date')[:25]