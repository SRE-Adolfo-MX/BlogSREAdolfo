from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from account.views import login_request, register_request

urlpatterns = [
    path('login/', login_request, name="Login"),
    path('logout/', LogoutView.as_view(template_name="accounts/logout.html"), name="Logout"),
    path('registrar/', register_request, name="Registrar"),
]
