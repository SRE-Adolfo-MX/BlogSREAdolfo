from django.urls import path
from AppCoder.views import show_html, about_me

urlpatterns = [
    path("show/", show_html),
    path("about_me/", about_me)
]