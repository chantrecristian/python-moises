from django.shortcuts import render,HttpResponse, redirect
from miapp.models import Article
from django.db.models import Q
from miapp.forms import FormArticle #Importamos el formulario desde forms.py
from django.contrib import messages #libreria mensajes flash

layout = """
    <h1>Sitio Web con Django | Aprendices ADSO</h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio">Inicio</a>
        </li>
        <li>
            <a href="/hola-mundo">Hola Mundo</a>
        </li>
        <li>
            <a href="/pagina-pruebas">Pagina</a>
        </li>
    </ul>
    <hr/>
"""

def index(request):
    html = """return HttpResponse(layout+
            <h1>Inicio</h1> )"""
    html += "</ul>"


    nombre= 'Carlos Gomez'

    #variable para bucles for utilizando listas
    lenguajes = ['JavaScript', 'Python', 'PHP', 'C#']

    return render(request, 'index.html',{
        'mi_variable':'****soy un dato que esta en la lista****',
        'nombre': nombre,
        'lenguajes': lenguajes,

    })
# Create your views here.
#request es un parametro que permite recibir datos de una url
#se le pasa a cada una de nuestras vistas
def hola_mundo(request):
    #le pasamos el render, la respuesta request y el nombre de la template
    return render(request, 'hola_mundo.html')

def pagina(request):
    return render(request, 'pagina.html')

def contacto(request, nombre):
    return HttpResponse(layout+f"<h2>Contacto {nombre}<h2>")

def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title, #title(nombre del modelo = title(nombre de la variable)
        content = content,
        public = public
    )
    #para guardar este articulo en la BD
    articulo.save()
    return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content}")

#copia de crear_articulo y lo llamamos save_articulo
def save_article(request): #no pasamos parametros por url y lo vamos a pasar por formulario
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']
        articulo = Article(
            title = title, #title(nombre del modelo) = title(nombre de la variable)
            content = content,
            public = public
        )
        #Para guardar este articulo en la BD
        articulo.save()
        return HttpResponse(f"Articulo creado: <strong> {articulo.title} - {articulo.content} </strong>")
    else:
        return HttpResponse(f"<h2> No se ha podido crear el articulo </h2>")
    
def create_article(request): #soporte para plantilla para visualizar el formulario
    return render(request, 'create_article.html')
    
def create_full_article(request):
    #Realizamos la comprobacion del metodo (post-get)
    if request.method == 'POST':
        #si llega datos por POST se debe:
        formulario = FormArticle(request.POST)
        #aqui podemos validar el formulario con un metodo is_valid
        if formulario.is_valid():
            #generamos una variable para recoger los datos del formulario
            data_form = formulario.cleaned_data #que son los datos limpios que nos llegan
            title = data_form.get('title') #lo puedo hacer asi o
            content = data_form['content']#lo puedo hacer asi
            public = data_form['public']

            articulo = Article(
                title = title, #title(nombre del modelo = title(nombre de la variable)
                content = content,
                public = public
                )
            #para guardar este articulo en la BD
            articulo.save()
            #crear mensajes flash(sesion que solo se muestra 1 vez)
            messages.success(request, f'ha creado correctamente el aritculo {articulo.id}')

            #Redireccionar la pagina a articulos despues de guardado
            return redirect('articulos')
            #return HttpResponse (title + ' -- ' + content + ' -- ' + str(public))
        
    else:
        #si nos llegan dator por POST debemos generar un formulario vacio
        formulario = FormArticle() #creamos una variable llamada formulario para instanciar el objeto
        #se carga la vista en htm
    return render(request, 'create_full_article.html', {
            'form' : formulario
    })

def articulo(request):
    #creams una variable llamada artiuclo y hacemos uso del modelo con objects
    #captura de excepcion
    try:
        articulo = Article.objects.get(title="Señor de los anillos", public=False)#get saca un solo registro de la BD
        response = f"Articulo:<br/> {articulo.id}. {articulo.title}"#se define la vista como se mostrar el articulo
    except:
        response = "<h1> Articulo no encontrado</h1>"
    return HttpResponse(response)

#actualizar articulo
def editar_articulo(request, id): #este id se pasa por la url del articulo que quiero editar
    #aqui se busca el articulo por el id
    #creamos una variable articulo
    articulo = Article.objects.get(pk=id)#se busca ese articulo por primary key pk = id
    #aqui se hace un cambio pero con valores dados desde aqui, como ejemplo
    articulo.title= "Iron Man"
    articulo.content = "La pelicula de Super heroes que lanzo la mayor franquicia de hollywood"
    articulo.public = True
    #asi se guardan los cambios
    articulo.save(    )
    return HttpResponse(f"Articulo Editado: {articulo.title} - {articulo.content}")

#mostrar articulos
def articulos(request):#creacion de la vista articulos
    #creamos una template para listar varios arituclos
    #1. hacemos la peticion a la base de datos
    #creamos la varibale artiuclos y lo llamamos articke, usamos objects para poder hacer una consulta
    articulos = Article.objects.all()#en este caso usamos el metodo get si no el all()para ssacar todos los datos
    #dentro de los articulos tenemos una lista de objetos array de objetos
    """
    #consultar con condiciones filter para filtara por un valor espeifico
    articulos = Article.objects.filter(title__contains = "Tiburon")

    #Realizar una consulta que muestre solo los esten publicados y excluya bajo una condicion
    articulos = Article.objects.filter(title__contains = "Tiburon").exclude(public=True)

    #consulta ejecutando SQL
    articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE title='Tiburon' AND public=1 ")

    #consulta ultilizacdo el OR con ORM
    articulos = Article.objects.filter(
        Q(title__contains="John") | Q(title__contains="Señor")
    )
    """
    return render(request,'articulos.html', {#pasamos el reuquest y la teplate articulo.html y como tercer parametro
        'articulos' : articulos #pasamos un diccionaio con las variables que deseamos mostrar
        })
#borrar articulo
def borrar_articulo(request, id):
    #asi selecciono el articulo dependiendo de lo que se pase por la url
    articulo = Article.objects.get(pk=id)
    #despues de seleccionado se borra de la siguiente manera
    articulo.delete()
    #redireccionar a la pagina de mostrar articulos para ver los cambios
    return redirect('articulos')