from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.contrib.auth.decorators import login_required



from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

# @login_required
# def profile(request):
#     return render(request,"accounts/profile.html")


def profile(request):
    return render(request, 'accounts/profile.html', {})
