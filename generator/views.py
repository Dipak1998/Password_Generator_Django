from django.shortcuts import render
from django.http import  HttpResponse
import random


# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length',12))

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('number'):
        characters.extend('0123456789')
    if request.GET.get('special'):
        characters.extend('!@#$%&*()')

    thispassword = ''

    for x in range(length):
        thispassword += random.choice(characters)


    return render(request, 'generator/password.html',{'password': thispassword})