from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.template import RequestContext
from django.urls import reverse
from .models import Category, Experience, Education, Abilitie, SpareTime, User, level
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



class AbilitieView(ListView):
    model = Abilitie
    template_name = 'cv/skill.html'

    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)
        context["users"] = User.objects.all()
        context["categories"] = Category.objects.filter(label='Skills')
        context['lvl'] = level
        return context


class SpareTimeView(ListView):
    model = SpareTime
    template_name = 'cv/sparetime.html'

    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)
        context["users"] = User.objects.all()
        context["categories"] = Category.objects.filter(label='SpareTime')
        return context


class ExperienceView(ListView):
    model = Experience
    template_name = 'cv/experience.html'
    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)
        context["users"] = User.objects.all()
        context["categories"] = Category.objects.filter(label='Experiences')
        return context


class EducationView(ListView):
    model = Education
    template_name= 'cv/education.html'


    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)
        context["users"] = User.objects.all()
        context["categories"] = Category.objects.filter(label='Education')
        return context


class XpView(DetailView):
    model = Experience

    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        context["users"] = User.objects.all()
        context["categories"] = Category.objects.all()
        return context

class EducView(DetailView):
    model = Education
    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        context["users"] = User.objects.all()
        context["categories"] = Category.objects.all()
        return context
