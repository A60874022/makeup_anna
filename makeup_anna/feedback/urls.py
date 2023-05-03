from django.urls import path

from . import views

app_name = 'feedback'

urlpatterns = [
    path('', views.feedback, name='feed'),
    path('customer/', views.customer, name='customer'),
]
