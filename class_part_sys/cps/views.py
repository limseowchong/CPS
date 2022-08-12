from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from datetime import date

from .models import Student, Module, Session, ClassParticipation

# Create your views here.
def index(request):
    return render(request, "cps/index.html", {
        "modules": list(Module.objects.all())
    })

def sessions(request, module_id):
    return render(request, "cps/sessions.html", {
        "module": Module.objects.get(pk=module_id),
        "sessions": list(Session.objects.filter(module_id=module_id))
    })

def generate_session(request, module_id):
    today = date.today()
    module = Module.objects.get(pk=module_id)

    new_session = Session()
    new_session.module = module
    new_session.date = today.strftime("%Y-%m-%d")
    new_session.save()

    return HttpResponseRedirect(reverse("sessions", args=(module.id,)))
