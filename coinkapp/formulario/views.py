from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views import generic

from .models import User
from .forms import FormularioUsuarios

class FormularioUserView(HttpRequest):
    
    def index(request):
        user = FormularioUsuarios()
        return render(request,"formulario/UserIndex.html",{
            "form": user
        })
    
    def procesar_formulario(request):
        user = FormularioUsuarios()
        if user.is_valid():
            user.save()
            user = FormularioUsuarios()
        
        return render(request, "formulario/formulario.html",{
            "form": user, "mensaje": "OK"
        })