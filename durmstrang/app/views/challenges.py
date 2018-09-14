from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import loader

from durmstrang.app.models import Challenge
from durmstrang.app.forms import ChallengeForm


@login_required(login_url="sign_in")
def index(request):
    challenges = Challenge.objects.filter(
        user_id=request.user.id).order_by("pk")
    template = loader.get_template("challenges/index.html")
    context = {"challenges": challenges}
    return HttpResponse(template.render(context, request))


def show(request):
    pass


def new(request):
    if request.method == "POST":
        form = ChallengeForm(request.POST, request.FILES)
        if form.is_valid():
            challenge = form.save(commit=False)
            challenge.user = request.user
            challenge.save()
            return HttpResponseRedirect("/challenges")
    else:
        form = ChallengeForm()
    context = {"form": form}
    template = loader.get_template("challenges/new.html")
    return HttpResponse(template.render(context, request))


def edit(request):
    pass


def destroy(request):
    pass
