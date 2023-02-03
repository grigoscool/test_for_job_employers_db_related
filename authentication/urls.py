from django.urls import path
from .views import LoginUser

app_name = 'auth'

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
]
