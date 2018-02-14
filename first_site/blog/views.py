from django.shortcuts import render
from django.views import generic

from .models import Post


class ListView(generic.ListView):
    template_name = 'blog/blog.html'

    def get_queryset(self):
        Post.objects.all().order_by('-date')[:25]