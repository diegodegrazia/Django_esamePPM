from . import views
from django.urls import path


urlpatterns = [
    path('<slug:post>/', views.postDetails, name='post_details'),
    path('<str:blog_name>', views.post_list, name='blog_home'),
    path('', views.BlogList.as_view(), name="home")
]