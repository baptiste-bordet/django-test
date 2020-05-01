from django.urls import path

from . import views

urlpatterns = [
    path('', viesws.index, name='index'),
]