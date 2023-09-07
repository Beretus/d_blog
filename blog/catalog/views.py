from django.shortcuts import render
from .models import CustomUser, Post, Comment, Like

# Create your views here.

def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
            }

    return render(request, 'base_generic.html', context=context)
