from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from .models import *


class IndexView(TemplateView):
    template_name = "index.html"


class AboutView(TemplateView):
    template_name = "about.html"


class AppView(DetailView):
    model = Application
    template_name = "application.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class BlogsView(ListView):
    model = Blog
    template_name = "blogs.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BlogView(DetailView):
    model = Blog
    template_name = "blog_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class AppliedView(ListView):
    model = Application
    template_name = "applied.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["applied"] = Application.objects.filter(status="Applied")
        return context


class ActiveView(ListView):
    model = Application
    template_name = "active.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active"] = Application.objects.filter(status='Active')
        return context


class DeadView(ListView):
    model = Application
    template_name = "dead.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dead'] = Application.objects.filter(status='Dead')
        return context


class CreateView(TemplateView):
    template_name = "add_view.html"