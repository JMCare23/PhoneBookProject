
from django.urls import path, include
from Phonebook import views

urlpatterns = [
    path('', views.contact_form, name='contact_insert'),
    path('<int:id>', views.contact_form, name='contact_update'),
    path('list/', views.contact_list, name = 'contact_list'),
    path('delete/<int:id>/', views.contact_delete, name = 'contact_delete')

]
