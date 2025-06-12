
from django.shortcuts import render, redirect
from .models import Pregunta, Respuesta, FeedbackFinal
from .mach import modelo 
from django.db.models import Sum

NUMERO_MAX_PREGUNTAS=20

def portada(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        edad = request.POST.get('edad')
        sexo = request.POST.get('sexo')
        Esta_de_examenes = request.POST.get('Esta_de_examenes')

        # Validación de "¿estás de exámenes?"
        if Esta_de_examenes == 'si':
            Esta_de_examenes = True
        elif Esta_de_examenes == 'no':
            Esta_de_examenes = False
        else:
            return render(request, 'core/portada.html', {'error': 'Por favor, selecciona una respuesta válida.'})

        # Validación del nombre repetido
        if Respuesta.objects.filter(nombre_usuario=nombre).exists():
            return render(request, 'core/portada.html', {'error': 'Ese nombre ya está en uso. Elige otro.'})
        
        sexo = request.POST.get('sexo')
        edad = request.POST.get('edad')

        if not sexo or not edad:
         return render(request, 'core/portada.html', {'error': 'Por favor, completa todos los campos.'})


        # Crear respuesta con edad y sexo
        Respuesta.objects.create(
            nombre_usuario=nombre,
            edad=int(edad) if edad else None,
            sexo=sexo,
            Esta_de_examenes=Esta_de_examenes
        )

        # Guardar el nombre en la sesión
        request.session['nombre_usuario'] = nombre
        return redirect('Preguntas', numero=1)

    return render(request, 'core/portada.html')

def Preguntas(request, numero):

    if 'nombre_usuario' not in request.session:
        return redirect('portada')

    nombre_usuario = request.session['nombre_usuario']

    try:
        numero = int(numero)
    except (ValueError, TypeError):
        return redirect('portada')

    if numero > NUMERO_MAX_PREGUNTAS:
        return redirect('Resultados')

    try:
        pregunta = Pregunta.objects.get(id=numero)
    except Pregunta.DoesNotExist:
        pregunta = None

    if request.method == 'POST':
       respuesta_texto = request.POST.get('respuesta', '').strip()  # Captura la respuesta sin espacios extra

    # Si la respuesta está vacía, mostramos el error y no guardamos nada
       if not respuesta_texto:
        return render(request, 'core/Preguntas.html', {
            'pregunta': pregunta,
            'numero': numero,
            'error': 'Por favor, escribe una respuesta válida antes de continuar.'
        })



       respuesta, created = Respuesta.objects.update_or_create(
            nombre_usuario=nombre_usuario,
            pregunta=pregunta,
            defaults={'respuesta': respuesta_texto}
        )

       modelo(numero)
       return redirect('Preguntas', numero=numero + 1)

    return render(request, 'core/Preguntas.html', {'numero': numero, 'pregunta': pregunta})


def Resultados(request):

    nombre_usuario = request.session.get('nombre_usuario')  
    if not nombre_usuario:
        return render(request, 'core/error.html', {'mensaje': 'No se encontró el usuario.'})

    Respuestas_usuario = Respuesta.objects.filter(nombre_usuario=nombre_usuario)
  
    total_puntuaciones = Respuestas_usuario.aggregate(Sum('puntuacion'))['puntuacion__sum']
    print(f" Total puntos de {nombre_usuario}: {total_puntuaciones}")

    if 20<= total_puntuaciones<= 29:
      mensaje="Usted no padece ansiedad en estos momentos"
      clase="mensaje-nada"
    elif  30<= total_puntuaciones <=38:
      mensaje="Tu resultado indica una leve presencia de señales asociadas a la ansiedad."
      clase="mensaje-bajo"
    elif  39<= total_puntuaciones <=53:
      mensaje="Tu resultado indica una presencia moderada de señales asociadas a la ansiedad."
      clase="mensaje-moderado"
    else :
      mensaje="Tu resultado indica una presencia elevada de señales asociadas a la ansiedad. Si sientes que lo necesitas, considera hablar con un profesional."
      clase="mensaje-alto"

    context = {
        'total_puntaciones': total_puntuaciones,
        'mensaje': mensaje,
        'clase' : clase
    }
    return render(request, 'core/Resultados.html',context)


def informacion(request):
    return render(request, 'core/informacion.html')




def feedback(request):
    nombre_usuario = request.session.get('nombre_usuario')

    if not nombre_usuario:
        return redirect('portada')
    
    if request.method == 'POST' and 'Ha_resultado_util' in request.POST:
        if not FeedbackFinal.objects.filter(nombre_usuario=nombre_usuario).exists():
            FeedbackFinal.objects.create(
                nombre_usuario=nombre_usuario,
                Ha_resultado_util=bool(int(request.POST.get('Ha_resultado_util'))),
                Se_ha_entendido=bool(int(request.POST.get('Se_ha_entendido'))),
                De_acuerdo_puntuaciones=bool(int(request.POST.get('De_acuerdo_puntuaciones'))),
                De_acuerdo_final=bool(int(request.POST.get('De_acuerdo_final'))),
                Lo_recomienda=bool(int(request.POST.get('Lo_recomienda')))
            )
        return redirect('portada')

    # Solo respuestas con puntuación no nula
    respuestas = Respuesta.objects.filter(
        nombre_usuario=nombre_usuario,
        puntuacion__isnull=False
    ).select_related('pregunta')

    puntuacion_total = sum(r.puntuacion or 0 for r in respuestas)

    return render(request, 'core/feedback.html', {
        'respuestas': respuestas,
        'puntuacion_total': puntuacion_total,
        'nombre_usuario': nombre_usuario,
    })

