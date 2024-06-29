from django.urls import path
from django.views.generic import TemplateView
from pages.views import rules

app_name = 'pages'

urlpatterns = [
    path('about/', TemplateView.as_view(template_name="pages/about.html"),
         name='about'),
    path('rules/', rules, name='rules'),
]
