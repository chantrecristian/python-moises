from django.db import models

# Create your models here.
#colocar los nombres de las entidades en singular

class Article(models.Model): #Entidad

    #propiedades *** Documentar cada tipo de dato
    title = models.CharField(max_length=150, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(default='null', verbose_name="Imagen", upload_to="articles")
    public = models.BooleanField(verbose_name="¿Publicado?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        #poner nombre en singular
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"

    def __str__(self):
        if self.public:
            public = "(publicado)"
        else:
            public = "(Privado)"
        return f"{self.title} {public}"
    
class Category(models.Model): #entidad
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    created_at = models.DateField()

    class Meta:
        #poner nombre en sigular
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"