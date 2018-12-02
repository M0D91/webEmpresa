from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    # de esta forma se puede pasar parametros dinamicos a las urls desde la vista
    # da igual cual sea el valor enviado en la vista, se interpretaran siempre
    # como una string por eso debemos castearlo para que sea un numero
    path('category/<int:category_id>/', views.category, name='category'),
]