from django.urls import path
from .views import create_article


urlpatterns = [
    path('article', create_article),
]