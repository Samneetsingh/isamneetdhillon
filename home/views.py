from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
# Create your views here.


class Home(View):
    template_name = 'home.html'

    def get(self, request):
        return render_to_response(template_name=self.template_name)