from django.urls import path
from . import views

urlpatterns = [

   path('', views.index, name="index"),# configuracion de ruta vacia viculdad al index
   path('inicio/', views.index, name="inicio"),#cuando encuentra la ruta de inicio
   path('registro/', views.register_page, name="register"),
   path('login/', views.login_page, name="login"),
   path('logout/', views.logout_user, name="logout"),
]     