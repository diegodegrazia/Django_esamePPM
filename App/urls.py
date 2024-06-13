from . import views
from django.urls import path


urlpatterns = [
    path('<str:blog_name>/<slug:slug>/add_comment', views.AddComment.as_view(), name='add_comment'),
    path('<str:blog_name>/<slug:slug>/<int:pk>/edit_comment', views.EditComment.as_view(), name='edit_comment'),
    path('<str:blog_name>/<slug:slug>/<int:pk>/delete_comment', views.CommentDeleteView.as_view(), name='delete_comment'),
    path('<str:blog_name>/<slug:slug>/edit_post', views.EditPost.as_view(), name="edit_post"),
    path('<str:blog_name>/<slug:slug>/delete_post', views.PostDeleteView.as_view(), name='delete_post'),
    path('<slug:slug>/edit_blog/', views.EditBlog.as_view(), name='edit_blog'),
    path('<slug:slug>/delete_blog/', views.BlogDeleteView.as_view(), name='delete_blog'),
    path('<str:blog_name>/<slug:slug>/', views.postDetails, name='post_details'),
    path('<str:blog_name>/add_post', views.AddPost.as_view(), name="add_post"),
    path('<str:blog_name>', views.post_list, name='blog_home'),
    path('add_blog/', views.AddBlog.as_view(), name='add_blog'),

    path('', views.BlogList.as_view(), name="home")
]