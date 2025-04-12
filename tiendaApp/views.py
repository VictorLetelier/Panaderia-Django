from django.shortcuts import render, redirect
from tiendaApp.forms import FormProducto
from tiendaApp.models import Producto
from tiendaApp.forms import FormUsuario
from tiendaApp.models import Usuario

# Create your views here.
def index(request):
    return render(request, 'index.html')


def listadoProducto(request):
    producto = Producto.objects.all()
    data = {'producto': producto}
    return render(request, 'index.html', data)

def agregarProyecto(request):
    form = FormProyecto()
    if request.method == 'POST' :
        form = FormProyecto(request.POST)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'modelFormApp/agregarProyecto.html', data)

def eliminarProyecto(request, id):
    proyecto = Proyecto.objects.get(id = id)
    proyecto.delete()
    return redirect('/proyectos')

def actualizarProyecto(request, id):
    proyecto = Proyecto.objetcs.get(id = id)
    form = FormProyecto(instance=proyecto)
    if request.method == 'POST' :
        form = FormProyecto(request.POST, instance=proyecto)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarProyecto.html', data)

    