from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead
from .forms import LeadForm

# Create your views here.

def leadlist(request):
    
    leads = Lead.objects.all()
    
    # return HttpResponse("YO")
    context = {
        "leads":leads
    }
    return render(request, "leads/leadlist.html", context)

def leadprofile(request,pk):
    print(pk)
    lead = Lead.objects.get(id=pk)
    print(lead)
    context = {
        "lead":lead
    }
    return render(request, "leads/leadprofile.html", context)

def createlead(request):
    form =LeadForm()
    if request.method == "POST":
        print('Post request recieved ')
        form = LeadForm(request.POST)
        if form.is_valid():
            print('Form is valid')
            print (form.cleaned_data)
    
    context = {
        "form":form
    }
    return render(request, "leads/createlead.html", context)