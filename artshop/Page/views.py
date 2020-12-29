from django.shortcuts import render
from django.http import HttpResponse


def top(request):
    return render(request, 'Page/first.html')


def pencil_art(request):
    return render(request, 'Page/pencil art.html')


def watercolor(request):
    return render(request, 'Page/watercolor.html')


def digital_art(request):
    return render(request, 'Page/digital art.html')


def cart(request):
    return render(request, 'Page/cart.html')


def like(request):
    return render(request, 'Page/like.html')


def login(request):
    return render(request, 'Page/login.html')


