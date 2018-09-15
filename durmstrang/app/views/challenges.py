from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.contrib import messages

from durmstrang.app.models import Challenge
from durmstrang.app.forms import ChallengeForm


@login_required(login_url="sign_in")
def index(request):
    challenges = Challenge.objects.filter(user_id=request.user.id).order_by("pk")
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
            messages.add_message(
                request, messages.SUCCESS, "Desafil criado com sucesso."
            )
            return HttpResponseRedirect("/")
        messages.add_message(request, messages.ERROR, "Campos inválidos.")
    else:
        form = ChallengeForm()
    context = {"form": form}
    template = loader.get_template("/challenges/new.html")
    return HttpResponse(template.render(context, request))


def edit(request, id):
    try:
        challenge_edit = Challenge.objects.get(id=id)
        if challenge_edit.user_id != request.user.id:
            messages.add_message(
                request, messages.ERROR, "Você não pode atualizar esse desafio."
            )
            return HttpResponseRedirect("/")

        if request.method == "POST":
            form = ChallengeForm(request.POST, request.FILES, instance=challenge_edit)
            if form.is_valid():
                challenge = form.save(commit=False)
                challenge.user = request.user
                challenge.save()
                messages.add_message(
                    request, messages.SUCCESS, "Desafil atualizado com sucesso."
                )
                return HttpResponseRedirect("/")
        else:
            form = ChallengeForm(instance=challenge_edit)
        context = {"form": form, "id": id}
        template = loader.get_template("/challenges/edit.html")
        return HttpResponse(template.render(context, request))
    except Challenge.DoesNotExist:
        messages.add_message(
            request, messages.ERROR, "Você não pode atualizar esse desafio."
        )
        return HttpResponseRedirect("/")


def destroy(request):
    pass
