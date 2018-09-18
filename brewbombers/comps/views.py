from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# This is the default landing page. This may be removed in the future.
def index(request):
    context = {}
    template = loader.get_template('comps/user_portal.html')
    return HttpResponse(template.render(context, request))


# This is the main admin page.
def brewbombers_admin(request):
    context = {}
    template = loader.get_template('comps/admin_portal.html')
    return HttpResponse(template.render(context, request))


# This is the judge adminstration page. You can add/remove/edit judges here.
def judge_admin(request):
    context = {}
    template = loader.get_template('comps/judge_mgmt.html')
    return HttpResponse(template.render(context, request))
