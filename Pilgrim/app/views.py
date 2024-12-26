from django.shortcuts import *
from django.http import *
from django.urls import *
from django.shortcuts import *
from .models import *
from django.urls import *

from django.http import JsonResponse
import random

def write_zapis(request):
    
    if request.method == 'POST':
        soderjanie = request.POST.get('soderjanie')

        if soderjanie: 
            zapis.objects.create(soderjanie=soderjanie)
            return redirect('all_zapis')
        
        else:
            return render(request, 'create_zapis.html')
    return render(request, 'create_zapis.html')

def all_zapis(request):
    zapisi = zapis.objects.all() 
    return render(request, 'all_zapis.html', {'zapisi': zapisi})

def delete_zapis(request, zapis_id):
    zzapis = get_object_or_404(zapis, id=zapis_id)
    zzapis.delete()
    return redirect('all_zapis')



