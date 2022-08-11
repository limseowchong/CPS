from django.shortcuts import render

from .models import Student, Module, Session, ClassParticipation

# Create your views here.
def index(request):
    return render(request, "cps/index.html", {
        "modules": list(Module.objects.all())
    })

def sessions(request, module_id):
    return render(request, "cps/sessions.html", {
        "sessions": list(Session.objects.filter(module_id=module_id))
    })