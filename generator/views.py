

# Create your views here.
from django.shortcuts import render
import random


def home(request): #домашняя страница
    return render(request, './home.html')

def password(request): #страница с выбором параметров пароля

    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length')) #берем данные из формы где выбираем длину пароля
    thepassword = ''

    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, './password.html', {'password': thepassword})


def description(request): #страница с описанием работы сайта
    return render(request, './description.html')


