from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from account.forms import UserRegisterForm

# Create your views here.
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)

        return redirect('/app/show')

    form = AuthenticationForm()
    contexto = {
        "form": form,
        "usuario": request.user
    }
    return render(request, template_name="accounts/login.html", context=contexto)

def register_request(request):
    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("/accounts/login")

    form = UserRegisterForm()
    contexto = {
        "form": form,
        "usuario": request.user
    }
    return render(request, template_name="accounts/registro.html", context=contexto)