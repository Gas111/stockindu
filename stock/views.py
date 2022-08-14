from django.shortcuts import render
from django.http import HttpResponse
from stock.models import Persona
from stock.models import Vestimenta
from stock.forms import IngForm
# Create your views here.

def lista(request):
    lista_personas=Persona.objects.all().order_by('apellido')
    return render(request,'lista.html',{'lista':lista_personas})

def ingresa(request):
    context={}

    if request.method=="POST":
        form=IngForm(request.POST)
        if form.is_valid():
            nombre=form.cleaned_data.get('nombre')
            apellido=form.cleaned_data.get('apellido')
            celular=form.cleaned_data.get('celular')
            dni=form.cleaned_data.get('dni')
            mail=form.cleaned_data.get('mail')
            reg=Persona.objects.create(nombre=nombre,apellido=apellido,celular=celular,dni=dni,mail=mail)
            reg.save()
            
    form=IngForm()#aca limpiamos el formulario
    context['form']=form    
    #lista_personas=Persona.objects.all().order_by('apellido')
    return render(request,'ingresa.html',context)#{'lista':lista_personas})

def busca(request):
    context={}

    if request.method=="GET":
        busquedadict=request.GET
        try:
            nombre=busquedadict.get('buscado')
        except:
            nombre=None
        buscareg=None
        if nombre is not None:    
            buscareg=Persona.objects.filter(nombre__contains=nombre)
            print(buscareg) 
    return render(request,'busca.html',{'lista':buscareg})


