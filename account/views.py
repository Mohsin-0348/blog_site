from django.shortcuts import render
from django.views.generic import ListView

from .models import User


class Users(ListView):
    model = User
    template_name = "tmp.html"
