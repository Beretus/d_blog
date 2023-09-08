from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import CustomUser, Post, Comment, LikePost, LikeComment

# Create your views here.

def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
            }

    return render(request, 'base_generic.html', context=context)

class PostDetailView(generic.DetailView):
    model = Post

    def post_detail_view(request, primary_key):
        post = get_object_or_404(Post, pk=primary_key)

        return render(request, 'catalog/post_detail.html', context={'post':post})
