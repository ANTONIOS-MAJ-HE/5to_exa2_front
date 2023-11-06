# agenda/urls.py
from django.urls import path
from . import views

urlpatterns = [
        path('api/contactos-list/', views.contactos_list, name='contactos_list'),
        path('api/contactos-list/<int:pk>', views.eliminar_contacto, name='eliminar-contacto'),
]
