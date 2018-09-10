from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.template import loader


@login_required(login_url='sign_in')
def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


@require_POST
def user_registration(request):
    try:
        user_by_email = User.objects.get(email=request.POST['email'])
        user_by_username = User.objects.get(email=request.POST['email'])

        if user_by_email or user_by_username:
            if request.GET['next']:
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect('/')

    except User.DoesNotExist:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        new_user = User.objects.create_user(
            username=username, email=email, password=password)
        new_user.save()
        login(request, new_user)
        if request.GET['next']:
            return HttpResponseRedirect(request.GET['next'])
        return HttpResponseRedirect('/')


@require_POST
def login_app(request):
    user = authenticate(username=request.POST['username'],
                        password=request.POST["password"])
    if user is not None:
        login(request, user)

    return HttpResponseRedirect('/')


@login_required(login_url='sign_in')
def logout_app(request):
    logout(request)

    return HttpResponseRedirect('/')


def sign_in(request):
    template = loader.get_template('login.html')
    context = {}
    return HttpResponse(template.render(context, request))


def sign_up(request):
    template = loader.get_template('sign_up.html')
    context = {}
    return HttpResponse(template.render(context, request))


def challenges(request):
    template = loader.get_template('challenges.html')
    context = {}
    return HttpResponse(template.render(context, request))
