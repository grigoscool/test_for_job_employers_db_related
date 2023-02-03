from django.urls import path
from .views import LoginUser, logout_view, RegisterUser

app_name = 'auth'

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),


]
