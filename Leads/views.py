from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead

# Create your views here.

def home(request):
    
    leads = Lead.objects.all()
    
    # return HttpResponse("YO")
    context = {
        "leads":leads
    }
    return render(request, "home.html", context)