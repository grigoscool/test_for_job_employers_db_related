from django.urls import path

from .views import home, show_employ, search, AddEmployer, EditEmploy, delete_employ


app_name = 'site'

urlpatterns = [
    path('', home, name='home'),
    path('employers/', show_employ, name='employ_list'),
    path('search_result/', search, name='search'),
    path('add_employer/', AddEmployer.as_view(), name='add_employ'),
    path('edit_employer/<int:pk>/', EditEmploy.as_view(), name='edit_employ'),
    path('delete_employer/<int:pk>/', delete_employ, name='delete_employ'),

]

