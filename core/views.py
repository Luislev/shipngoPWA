from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from . import forms

# Create your views here.

def home(request):
    return render(request, 'home.html')

def sign_up(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password, email=email)
            login(request, user, backend='django.contrib.auth.backends.Modelbackend')
            return redirect('/')
    else:
        form = forms.SignUpForm()
    return render(request, 'sign_up.html', {'form': form})