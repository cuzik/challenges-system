from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader


@login_required(login_url="sign_in")
def index(request):
    template = loader.get_template("index.html")
    context = {}
    return HttpResponse(template.render(context, request))
