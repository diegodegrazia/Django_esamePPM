from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import UserAuthenticationForm
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


class UserLoginView(LoginView):
    authentication_form = UserAuthenticationForm
    template_name = 'login.html'
