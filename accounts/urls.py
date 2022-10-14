from django.urls import path

from . import views

from .views import SignUpView
from .views import profile

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    # path("profile", views.profile, name="profile"),
]