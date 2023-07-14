from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    send_mail('Hola soy Reyser Zapata', 
              'Este es un correo enviado automaticamente con Django.',
              'rzapata@unsa.edu.pe',
              ['koferaf572@kameili.com'],
              fail_silently=False)
    return render(request, 'send/index.html')
