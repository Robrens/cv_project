from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.template import RequestContext
from django.urls import reverse
from .models import Category, Experience, User
from datetime import datetime


class IndexView (ListView):
    model = User

    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)
        context["users"] = User.objects.all()
        context["categories"] = Category.objects.all()
        return context


class CategoryView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        context["users"] = User.objects.all()
        context["categories"] = Category.objects.all()
        return context


class XpView(DetailView):
    model = Experience

    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        context["users"] = User.objects.all()
        context["categories"] = Category.objects.all()
        return context

