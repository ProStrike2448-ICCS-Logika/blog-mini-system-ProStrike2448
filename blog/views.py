from django.http import HttpRequest
from django.shortcuts import render

from .models import Post


def post_list(request: HttpRequest):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }

    return render(request=request, template_name='post_list.html', context=context)
