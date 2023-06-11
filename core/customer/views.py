from django.shortcuts import render, redirect
from core.customer import forms
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def home(request):
    return redirect(reverse('customer:profile'))

def profile_page(request):
    user_form = forms.BasicUserForm()

    return render(request, 'customer/profile.html'), {
        "user_form": user_form
    }
