from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views import generic

@login_required
def site(request):
    profile = request.user.profile
    return HttpResponseRedirect(profile.site)

class SignUp(generic.CreateView):
    pass
