from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate


def index(request):
    user = authenticate(username='john', password='secret')
    if user is not None:
        return HttpResponse("Hello, world. You're at the polls index.")
    else:
        return redirect('login')


def login(request):
    return HttpResponse("login.")
