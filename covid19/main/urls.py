

from django.urls import path
from main.views import homePage

urlpatterns = [
    path('', homePage),
]
