from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'generator/index.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    thePassword = 'testing'

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if request.GET.get('special'):
        characters.extend('!@#$%^&*()_~+{}:"<>?,./;')

    if request.GET.get('numbers'):
        characters.extend('0123456789')

    length = int(request.GET.get('length',14))

    thePassword = ''
    for x in range(length):
        thePassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thePassword})