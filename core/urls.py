from django.urls import path
from . import views  # Importa las vistas desde el archivo views.py de tu aplicación

urlpatterns = [
    path('', views.portada, name='portada'),  # Ruta a la vista `home`
    path('Preguntas/<int:numero>/', views.Preguntas, name='Preguntas'),
    path('Resultados/', views.Resultados, name='Resultados'),
     path('informacion/', views.informacion, name='informacion'),
     path('feedback/', views.feedback, name='feedback'),
]
