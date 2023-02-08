from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('get_posts/', views.show_posts, name='get_posts'),
    path('send_posts/', views.send_posts, name='send_posts'),
    path('send_fio/', views.send_my_fio, name='send_api_fio'),

]

