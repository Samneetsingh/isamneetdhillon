from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.


class Home(View):
    def get(self, request):
        return HttpResponse("<h2>Begin</h2><h2>End</h2>")