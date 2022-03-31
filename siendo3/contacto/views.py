from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
    formulario_contacto = FormularioContacto()
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            
            email= EmailMessage("mensaje desde app siendo tres",
            "el usuairo con {} con email {} escribe lo siguiente:\n\n{}".format(nombre,email,contenido),
            "",["julian.marinc@udea.edu.co"],reply_to=[email])
            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")

    return render(request,"contacto/contacto.html",{"miFormulario":formulario_contacto})