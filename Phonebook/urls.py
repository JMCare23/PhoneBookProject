
from django.urls import path, include
from Phonebook import views


urlpatterns = [
    path('',views.contact_api),
    path('<int:id>', views.contact_api)
]
