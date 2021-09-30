from django.contrib import admin
from django.urls import path
from .views import PacientsListView, get_pacient

urlpatterns = [
    path('pacients/', PacientsListView.as_view()),
    path('pacient/', get_pacient)
]