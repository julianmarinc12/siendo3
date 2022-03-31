from django.urls import path
from .views import VResgistro,cerrar_sesion, logear
 

urlpatterns = [
    path('',VResgistro.as_view(), name="autenticacion"),
    path('cerrar_sesion',cerrar_sesion, name="cerrar_sesion"),
    path('logear',logear, name="logear"),
       
]
