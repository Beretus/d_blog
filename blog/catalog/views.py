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
    template_name = 'catalog/post_detail.html'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        author = post.author
        same_author_posts = Post.objects.filter(author=author).exclude(pk=post.pk)[:3]
        context['same_author_posts'] = same_author_posts
        return context


class CustomUserListView(generic.ListView):
    model = CustomUser
