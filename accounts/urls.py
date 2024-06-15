from . import views
from django.urls import path
from .views import UserLoginView, register


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', register, name='register'),
]
