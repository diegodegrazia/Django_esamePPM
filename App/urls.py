from . import views
from django.urls import path


urlpatterns = [
    path('<slug:post>/', views.postDetails, name='post_details'),
    path('', views.PostList.as_view(), name='home'),
]