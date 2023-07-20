from django.urls import path
from . import views
from job_search.views import *

app_name = 'job_search'

urlpatterns = [
    path('', IndexView.as_view()),
    path('about/', AboutView.as_view()),
    path('blog/', BlogsView.as_view()),
    path('blog/<slug:slug>/', BlogView.as_view()),
    path('app/<int:pk>/', AppView.as_view(), name='application'),
    path('create/', CreateView.as_view(), name='create')
]