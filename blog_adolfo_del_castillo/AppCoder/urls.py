from django.urls import path
from AppCoder.views import show_html, about_me, crear_usuario_form, crear_publicacion_form, mostrar_usuarios, busqueda_usuario, busqueda_publicacion, mostrar_publicaciones

urlpatterns = [
    path("about_me/", about_me),
    path("crear_usuario_form/", crear_usuario_form),
    path("crear_publicacion_form/", crear_publicacion_form),
    path("usuarios/", mostrar_usuarios),
    path("busqueda_usuario/", busqueda_usuario),
    path("publicaciones/", mostrar_publicaciones),
    path("busqueda_publicacion/", busqueda_publicacion),
]