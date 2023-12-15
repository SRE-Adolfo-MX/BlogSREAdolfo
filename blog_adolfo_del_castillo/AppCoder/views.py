from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime, date
from AppCoder.models import Usuario, Publicacion, Comentarios
from AppCoder.forms import UsuarioForms, BusquedaUsuarioForms, PublicacionForms, ComentarioForms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def show_html(request):
    
    contexto = {
        "nombre": "Welcome",
        "usuario": request.user,
    }
    return render(request, template_name="accounts/welcome.html", context=contexto)

def invalid_access(request):
    
    contexto = {
        "nombre": "Welcome",
        "usuario": request.user,
    }
    return render(request, template_name="accounts/invalid_access.html", context=contexto)

def about_me(request):
    contexto = {
        "usuario": request.user
    }
    return render(request, template_name="AppCoder/about_me.html", context=contexto)

def crear_usuario_form(request):
    if request.method == "POST":
        usuario_formulario = UsuarioForms(request.POST)
        if usuario_formulario.is_valid():
            informacion = usuario_formulario.cleaned_data
            usuario_crear = Usuario(nombreUsuario = informacion["nombreUsuario"], nombre = informacion["nombre"], apellido = informacion["apellido"], email = informacion["email"])
            usuario_crear.save()
            return redirect("/app/show/")

    usuario_formulario = UsuarioForms()
    contexto = {
        "form": usuario_formulario,
        "usuario": request.user
    }

    return render(request, template_name="AppCoder/crear_usuario.html", context=contexto)

@login_required
def crear_publicacion_form(request):
    if request.method == "POST":
        publicacion_formulario = PublicacionForms(request.POST)
        if publicacion_formulario.is_valid():
            informacion = publicacion_formulario.cleaned_data
            publicacion_crear = Publicacion(nombreUsuario = request.user, titulo = informacion["titulo"], comentario = informacion["comentario"], fecha = date.today())
            publicacion_crear.save()
            return redirect("/app/publicaciones/")

    publicacion_formulario = PublicacionForms()
    contexto = {
        "form": publicacion_formulario,
        "usuario": request.user
    }

    return render(request, template_name="AppCoder/crear_publicacion.html", context=contexto)

@login_required()
@staff_member_required(login_url="/app/invalid_access/")
def mostrar_usuarios(request):
    usuarios = User.objects.all()
    contexto = {
        "usuarios": usuarios,
        "form": BusquedaUsuarioForms(),
        "usuario": request.user
    }
    return render(request, template_name="AppCoder/usuarios.html", context=contexto)

def busqueda_usuario(request):
    nombreUsuario = request.GET["idUsuario"]
    usuario = User.objects.filter(username__icontains=nombreUsuario)
    contexto = {
        "usuarios": usuario,
        "form": BusquedaUsuarioForms(),
        "usuario": request.user
    }

    return render(request, template_name="AppCoder/usuarios.html", context=contexto)


def mostrar_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    contexto = {
        "publicaciones": publicaciones,
        "nombre": "Welcome",
        "form": BusquedaUsuarioForms(),
        "usuario": request.user
    }
    return render(request, template_name="AppCoder/publicaciones.html", context=contexto)

def busqueda_publicacion(request):
    nombreUsuario = request.GET["idUsuario"]
    publicacion = Publicacion.objects.filter(nombreUsuario__icontains=nombreUsuario)
    contexto = {
        "publicaciones": publicacion,
        "form": BusquedaUsuarioForms(),
        "usuario": request.user
    }

    return render(request, template_name="AppCoder/publicaciones.html", context=contexto)

def eliminar_publicacion(request):
    idPublicacion = request.GET("id")
    publicacion = Publicacion.objects.get(id=idPublicacion)
    publicacion.delete()
    return redirect("AppCoder/publicaciones.html")


class PublicacionDetalle(LoginRequiredMixin, DetailView):
    model = Publicacion
    template_name = "AppCoder/publicacion_detalle.html"

class PublicacionActualizar(UpdateView):
    model = Publicacion
    success_url = "/app/publicaciones/"
    template_name = "AppCoder/crear_publicacion.html"
    fields = ["titulo", "comentario"]

class PublicacionEliminar(DeleteView):
    model = Publicacion
    template_name = "AppCoder/eliminar_publicacion.html"
    success_url = "/app/publicaciones/"

class CrearComentario(CreateView):
    model = Comentarios
    success_url = "AppCoder/publicacion_detalle.html"
    template_name = "AppCoder/crear_publicacion.html"
    fields = ["idPublicacion", "comentario"]

def comentar_publicacion(request):
    if request.method == "POST":
        publicacion_formulario = ComentarioForms(request.POST)
        if publicacion_formulario.is_valid():
            informacion = publicacion_formulario.cleaned_data
            publicacion_crear = Comentarios(nombreUsuario = request.user, comentario = informacion["comentario"], fecha = date.today())
            publicacion_crear.save()
            return redirect("/app/publicaciones/")

    publicacion_formulario = ComentarioForms()
    contexto = {
        "form": publicacion_formulario,
        "usuario": request.user
    }

    return render(request, template_name="AppCoder/crear_publicacion.html", context=contexto)