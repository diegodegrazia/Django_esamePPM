from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import PostCreationForm, CommentCreationForm, PostEditForm, CommentEditForm, BlogCreationForm, BlogEditForm
from .models import Post, Blog, Comment
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


def postDetails(request, blog_name, slug):
    blog = get_object_or_404(Blog, name=blog_name)
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html', {"blog": blog, "post": post})


class AddBlog(CreateView):
    model = Blog
    form_class = BlogCreationForm
    template_name = 'add_blog.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditBlog(UpdateView):
    model = Blog
    form_class = BlogEditForm
    template_name = 'edit_blog.html'
    success_url = reverse_lazy('home')


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'delete_blog.html'

    def get_success_url(self):
        return reverse_lazy('home')


class AddPost(CreateView):
    model = Post
    form_class = PostCreationForm
    template_name = 'add_post.html'

    def get_success_url(self):
        return reverse_lazy('blog_home', kwargs={'blog_name': self.object.blog.name})

    # form_valid serve per associare, in fase di creazione del post,
    # post.blog al relativo blog in cui mi trovo. L'edit o il delete non ne hanno
    # bisogno perché al campo è già stato dato un valore.

    def form_valid(self, form):
        blog = get_object_or_404(Blog, name=self.kwargs['blog_name'])
        form.instance.blog = blog
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPost(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'edit_post.html'

    def get_success_url(self):
        return reverse_lazy('blog_home', kwargs={'blog_name': self.object.blog.name})


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'

    def get_success_url(self):
        return reverse_lazy('blog_home', kwargs={'blog_name': self.object.blog.name})


class AddComment(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'add_comment.html'

    def get_success_url(self):
        return reverse_lazy('post_details',
                            kwargs={'blog_name': self.object.post.blog.name, 'slug': self.object.post.slug})

    # form_valid serve per associare, in fase di creazione del commento,
    # comment.post al relativo post in cui mi trovo. L'edit o il delete non ne hanno
    # bisogno perché al campo è già stato dato un valore.
    def form_valid(self, form):
        post = get_object_or_404(Post, slug=self.kwargs['slug'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditComment(UpdateView):
    model = Comment
    form_class = CommentEditForm
    template_name = 'edit_comment.html'

    def get_success_url(self):
        return reverse_lazy('post_details',
                            kwargs={'blog_name': self.object.post.blog.name, 'slug': self.object.post.slug})


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'delete_comment.html'

    def get_success_url(self):
        return reverse_lazy('post_details',
                            kwargs={'blog_name': self.object.post.blog.name, 'slug': self.object.post.slug})
