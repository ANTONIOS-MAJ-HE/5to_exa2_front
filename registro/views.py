from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Contacto
from .forms import ContactoForm
import requests

def contactos_list(request):
    try: 
        reponse=requests.get('http://127.0.0.1:8070/api/contactos/')
        data= reponse.json()
        return render(request, 'agenda/contactos_list.html',{'datos': data})
    
    except Exception as  e :  
        print(e)
        return render(request, 'error.html')
    
def eliminar_contacto(request, pk):
    try: 
        response=requests.delete(f'http://127.0.0.1:8070/api/contactos/{pk}')
        if response.status_code==204:
            return redirect('./')
        else:
            return render(request, 'error.html')
    except Exception as  e :  
        print(e)
        return render(request, 'error.html')    
