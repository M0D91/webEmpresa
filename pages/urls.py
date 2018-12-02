from django.urls import path
from . import views

urlpatterns = [
    # de esta forma se puede pasar parametros dinamicos a las urls desde la vista
    # da igual cual sea el valor enviado en la vista, se interpretaran siempre
    # como una string por eso debemos castearlo para que sea un numero
    path('<int:page_id>/<slug:page_slug>/', views.page, name='page'),
]