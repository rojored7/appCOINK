from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.FormularioUserView.index, name="index"),
    path("procesar_formulario/", views.FormularioUserView.procesar_formulario, name="form"),
    path("SaveUser/", views.FormularioUserView.procesar_formulario, name="save"),
    path("UserList/",views.FormularioUserView.UserList, name="list")
]
