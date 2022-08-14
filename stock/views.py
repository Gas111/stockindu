from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def lista(request):
    return render(request,'lista.html')#,{'lista':lista_personas})

