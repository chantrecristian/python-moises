from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
"""ELIMINAR EN CASCADA:cuando creemos una clave foranea utilizando esta opcion, elimina las filas de referencia
 en la tabla secundaria cuando la fila referenciada se elimina en la primera tabla primaria que tiene una clave
 primaria.

ACTUALIZAD EN CASCADA:cuando creamos una clave eterna utilizando ACTUALIZACION CASCADA , las filas de referencia
se  van a actualizar  en la tabla secundaria cuando la fila referenciada se actualiza en la tabla primaria 
que tiene  una clave primaria  
"""

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.CharField(max_length=255, verbose_name='Descripcion')
    created_at = models.DateField(auto_now_add=True, verbose_name='Creado el') 

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return  self.name
    

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Titulo')
    content = RichTextField(verbose_name='Contendio')
    image = models.ImageField(default='null', verbose_name='Imagen', upload_to="articles")
    public = models.BooleanField(verbose_name='¿Publicado?')
    user = models.ForeignKey(User,editable=False, verbose_name='Usuario', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name='Categorias', blank=True, related_name="articles")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el') 
    update_at = models.DateTimeField(auto_now=True, verbose_name='Editado el') 


    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        ordering = ['-created_at']
        

    def __str__(self):
        return  self.title
    