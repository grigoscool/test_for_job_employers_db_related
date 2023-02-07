from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('users/', views.show_users, name='api_users'),
]
