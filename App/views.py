from django.shortcuts import render
from .models import Post, Blog
from django.views import generic
from django.shortcuts import get_object_or_404


def index(request):
    template = 'base.html'
    return render(request, template)


class BlogList(generic.ListView):
    queryset = Blog.objects.order_by('-created_on')
    template_name = 'index.html'


def post_list(request, blog_name):
    blog = get_object_or_404(Blog, name=blog_name)
    posts = Post.objects.filter(blog=blog).order_by('-created_on')
    context = {
        'blog': blog,
        'posts': posts
    }
    return render(request, 'blog_home.html', context)


def postDetails(request, post):
    post = get_object_or_404(Post, slug=post)
    return render(request, 'post_detail.html', {"post": post})
