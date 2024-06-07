from django.shortcuts import render
from .models import Post
from django.views import generic


# Vista che mi restituisce una lista di post pubblicati
# ed in ordine di creazione, dal più recente al più vecchio.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


# Vista che mi fa visualizzare tutto il contenuto del post se clicco "read more".

class DetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
