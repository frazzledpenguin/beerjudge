from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import addUserForm
from django.contrib.auth.models import User


# This is the default landing page. This may be removed in the future.
def index(request):
    context = {}
    template = loader.get_template('comps/user_portal.html')
    return HttpResponse(template.render(context, request))


# This is the main admin page.
def brewbombers_admin(request):
    context = {
                'nav_class': 'dashboard' # Sets sidebar class to active in template.
              }
    template = loader.get_template('comps/admin_portal.html')
    return HttpResponse(template.render(context, request))


# This is the judge adminstration page. You can add/remove/edit judges here.
def judge_admin(request):
    if request.method == "POST":
        addjudgeform = addUserForm(request.POST)
        if addjudgeform.is_valid():
            new_user = User.objects.create_user(**addjudgeform.cleaned_data)
            return HttpResponseRedirect('/judge_admin')
        else:
            return HttpResponseRedirect('/judge_admin?error=nameError')
    else:
        addjudgeform = addUserForm()

    context = {
                'nav_class': 'judge',     # Sets sidebar class to active in template.
                'addjudge': addjudgeform  # The add judge form
              }
    template = loader.get_template('comps/judge_mgmt.html')
    return HttpResponse(template.render(context, request))
