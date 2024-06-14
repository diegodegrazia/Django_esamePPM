
from django.db import IntegrityError
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


class BlogListView(generic.ListView):
    queryset = Blog.objects.order_by('-created_on')
    template_name = 'index.html'


class PersonalBlogListView(generic.ListView):
    template_name = 'index.html'

    def get_queryset(self):
        queryset = Blog.objects.filter(author=self.request.user).order_by('-created_on')
        return queryset


class PersonalPostListView(generic.ListView):
    template_name = 'personal_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        username = self.kwargs['username']
        blog_name = self.kwargs['blog_name']
        return Post.objects.filter(author__username=username, blog__name=blog_name).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.kwargs['username']
        blog_name = self.kwargs['blog_name']
        context['blog'] = get_object_or_404(Blog, name=blog_name)
        context['postDrafted'] = Post.objects.filter(author__username=username, blog__name=blog_name, status=0).order_by('-created_on')
        context['postPublished'] = Post.objects.filter(author__username=username, blog__name=blog_name, status=1).order_by('-created_on')
        return context


def post_list(request, blog_name):
    blog = get_object_or_404(Blog, name=blog_name)
    posts = Post.objects.filter(blog=blog, status=1).order_by('-created_on')
    context = {
        'blog': blog,
        'posts': posts
    }
    return render(request, 'blog_home.html', context)


def postDetails(request, blog_name, slug):
    blog = get_object_or_404(Blog, name=blog_name)
    post = get_object_or_404(Post, slug=slug, blog=blog)
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
        try:
            blog = get_object_or_404(Blog, name=self.kwargs['blog_name'])
            form.instance.blog = blog
            form.instance.author = self.request.user
            return super().form_valid(form)
        except IntegrityError as e:
            # Cerca i messaggi di violazione dei vincoli nel testo dell'eccezione
            if 'unique_title_per_blog' in str(e):
                form.add_error('title', "Title already used in this blog.")
            if 'unique_slug_per_blog' in str(e):
                form.add_error('slug', "Slug already used in this blog.")
            return self.form_invalid(form)


class EditPost(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'edit_post.html'

    def get_success_url(self):
        return reverse_lazy('blog_home', kwargs={'blog_name': self.object.blog.name})

    # get_queryset() e get_object() servono per non rompere lo uniqueConstraint di Post
    def get_queryset(self):
        return Post.objects.filter(blog__name=self.kwargs['blog_name'])

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        return get_object_or_404(queryset, slug=self.kwargs['slug'])

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError as e:
            if 'unique_title_per_blog' in str(e):
                form.add_error('title', "Title already used in this blog.")
            if 'unique_slug_per_blog' in str(e):
                form.add_error('slug', "Slug already used in this blog.")
            return self.form_invalid(form)


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'

    def get_success_url(self):
        return reverse_lazy('blog_home', kwargs={'blog_name': self.object.blog.name})

    # get_queryset() e get_object() servono per non rompere lo uniqueConstraint di Post
    def get_queryset(self):
        return Post.objects.filter(blog__name=self.kwargs['blog_name'])

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        return get_object_or_404(queryset, slug=self.kwargs['slug'])


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
        post = get_object_or_404(Post, slug=self.kwargs['slug'], blog__name=self.kwargs['blog_name'])
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
