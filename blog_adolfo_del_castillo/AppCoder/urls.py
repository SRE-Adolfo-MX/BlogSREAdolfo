from django.urls import path
from AppCoder.views import show_html, about_me, crear_usuario_form, crear_publicacion_form, mostrar_usuarios, busqueda_usuario, busqueda_publicacion, mostrar_publicaciones, PublicacionDetalle, PublicacionActualizar, PublicacionEliminar, invalid_access, CrearComentario, comentar_publicacion

urlpatterns = [
    path("show/", show_html),
    path("invalid_access/", invalid_access),
    path("about_me/", about_me),
    path("crear_usuario_form/", crear_usuario_form),
    path("crear_publicacion_form/", crear_publicacion_form),
    path("usuarios/", mostrar_usuarios),
    path("busqueda_usuario/", busqueda_usuario),
    path("publicaciones/", mostrar_publicaciones),
    path("busqueda_publicacion/", busqueda_publicacion),
    path("publicacion/<int:pk>", PublicacionDetalle.as_view(), name="PublicacionDetalle"),
    path("editar/<int:pk>", PublicacionActualizar.as_view(), name="PublicacionEditar"),
    path("eliminar/<int:pk>", PublicacionEliminar.as_view(), name="PublicacionEliminar"),
    path("comentar_publicacion/<int:pk>", CrearComentario.as_view(), name="ComentarPublicacion"),
    
]