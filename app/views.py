from django.shortcuts import render
from app.models import App, Equipo, Nosotros

def inicio(request):
	apps = App.objects.all()
	equipos = Equipo.objects.all()
	nosotros = Nosotros.objects.all()
	return render(request, 'inicio.html',{ 'apps':apps, 'equipos':equipos, 'nosotros':nosotros })