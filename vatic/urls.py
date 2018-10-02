from django.urls import path
from . import views

urlpatterns = [
    path('', views.vw_index, name='index'),
]