from django.shortcuts import render
from .models import Post
from django.views import generic
from django.shortcuts import get_object_or_404


def index(request):
    template = 'base.html'
    return render(request, template)


# Vista che mi restituisce una lista di post pubblicati
# ed in ordine di creazione, dal più recente al più vecchio.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


# Vista che mi fa visualizzare tutto il contenuto del post se clicco "read".

def postDetails(request, post):
    post = get_object_or_404(Post, slug=post)
    return render(request, 'post_detail.html', {"post": post})
