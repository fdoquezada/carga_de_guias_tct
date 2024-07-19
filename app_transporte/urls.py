from django.conf import settings
from django.conf.urls.static import static
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subir/', views.subir_imagen, name='subir_imagen'),
    path('mis-imagenes/', views.listar_imagenes, name='listar_imagenes'),
    path('editar/<int:pk>/', views.editar_imagen, name='editar_imagen'),
    path('eliminar/<int:pk>/', views.eliminar_imagen, name='eliminar_imagen'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro, name='registro'),
  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)