from django.urls import path
from . import views
from job_search.views import *

app_name = 'job_search'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('links/', LinksView.as_view(), name='links'),
    path('blog/', BlogsView.as_view(), name='blog'),
    path('blog/<slug:slug>/', BlogView.as_view(), name='blog'),
    path('app/<int:pk>/', AppView.as_view(), name='app'),
    path('create/', CreateView.as_view(), name='create'),
    path('applied/', AppliedView.as_view(), name='applied'),
    path('active/', ActiveView.as_view(), name='active'),
    path('dead/', DeadView.as_view(), name='dead'),
]