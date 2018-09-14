# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Notas

def home(request):
	notas = Notas.objects.order_by('-creado')
	ctx = {'notas': notas, 'numero': 6}
	return render(request, 'home.html', ctx)

def crear(request):
	texto = request.POST.get('texto')
	nota = Notas(texto=texto)
	nota.save()
	return redirect('home')

def archivar(request, id):
	nota = Notas.objects.get(pk=id)
	nota.archivado = True
	nota.save()
	return redirect('home')
