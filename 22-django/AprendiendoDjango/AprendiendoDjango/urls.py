"""AprendiendoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#importar app con mis vistas
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #ruta para pagina de inicio -> index
    path('', views.index, name="index"),
    #otro cambio
    path("inicio/", views.index, name="inicio"),
    #creacion de ruta
    path('hola-mundo/', views.hola_mundo, name="hola_mundo"),
    path('pagina/', views.pagina, name="pagina"),

    path('contacto/<str:nombre>', views.contacto, name="contacto"),
    path('crear_articulo/<str:title>/<str:content>/<str:public>', views.crear_articulo, name="crear_articulo"),
    path('articulo/', views.articulos, name="articulo"),
    #ruta para deutar un arituclo y se le pasa el id por la url
    path('editar-articulo/<int:id>', views.editar_articulo),#el name no es obligatorio
    #ruta para mostrar todos los articulos de la BD
    path('articulos/', views.articulos, name="articulos"),
    #ruta borrar articulo
    path('borrar-articulo/<int:id>', views.borrar_articulo, name="borrar"),
    #ruta para formularios
    path('save-article/', views.save_article, name="save"),
    path('create-article/', views.create_article, name="create"),
    path('create-full-article/', views.create_full_article, name="create_full"),
]
