from django.urls import path
from .views import home, show_employ


urlpatterns = [
    path('', home, name='home'),
    path('employers', show_employ, name='employ_list'),
]
