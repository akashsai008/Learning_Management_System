from django.urls import path
from . import views

urlpatterns = [
    path('custom-action/', views.custom_action_view, name='custom-action-url'),
]
