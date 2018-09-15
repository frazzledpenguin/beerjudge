from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    context = {}
    template = loader.get_template('comps/user_portal.html')
    return HttpResponse(template.render(context, request))

    
def brewbombers_admin(request):
    context = {}
    template = loader.get_template('comps/admin_portal.html')
    return HttpResponse(template.render(context, request))
