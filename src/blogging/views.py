from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

def hello_world(request):
    name = request.GET.get("name")
    if name is None:
        return HttpResponse("Hello world!")
    else:
        return HttpResponse("Hello " + name)


@login_required
def home(request):
  return HttpResponse("Hello world!")
    #latest_movies = Movie.objects.all().order_by("-release_date")
    #context = {'movies': latest_movies[:5]}
    #return render(request, "home.html", context)
