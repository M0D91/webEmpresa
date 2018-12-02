from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    # print('Tipo peticion: {}'.format(request.method))
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')

            #Suponemos que todo va bien, enviamos el correo y redireccionamos
            # return redirect('/contact/?ok')
            email = EmailMessage(
                'La Caffettiera: nuevo mensaje', #asunto
                'De {} <{}>\n\nEscribió:\n\n{}'.format(name,email,content), #cuerpo
                'no-contestar@coño.ya',   #email_origen
                ['msl.snzn@gmail.com'],         #email_destino
                reply_to=[email]
            )

            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                 # Algo no ha ido bien,redireccion a fail   
                return redirect(reverse('contact')+"?fail")

    return render(request, "contact/contact.html", {'form':contact_form})