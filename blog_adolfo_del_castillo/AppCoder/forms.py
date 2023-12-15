from django import forms

class UsuarioForms(forms.Form):
    nombreUsuario = forms.CharField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class BusquedaUsuarioForms(forms.Form):
    idUsuario = forms.CharField()

class PublicacionForms(forms.Form):
    titulo = forms.CharField()
    comentario = forms.CharField(widget=forms.Textarea)
    
class ComentarioForms(forms.Form):
    comentario = forms.CharField(widget=forms.Textarea)