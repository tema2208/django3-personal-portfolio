from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all() # джанго импортирует все данные из базы данных
    return render(request, 'portfolio/home.html', {'projects': projects}) # если передать просто строку то хуйня будет
