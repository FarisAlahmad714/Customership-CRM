from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm , LeadModelForm

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
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/leads")
    context = {
        "form": form
    }
    return render(request, "leads/createlead.html", context)

def updatelead(request,pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form= LeadModelForm(request.POST , instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "lead":lead,
        "form": form
    }
    return render (request, "leads/updatelead.html" , context)

def deletelead(request , pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect ("/leads")
# def updatelead(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#                 first_name = form.cleaned_data['first_name']
#                 last_name = form.cleaned_data['last_name']
#                 age = form.cleaned_data['age']
#                 agent = Agent.objects.first()
#                 # update 
#                 lead.first_name = first_name
#                 lead.last_name = last_name
#                 lead.age = age
#                 lead.agent = agent
#                 lead.save()
#                 return redirect("/leads")
    # context = {
    #     "lead":lead,
    #     "form": form
    # }
    # return render (request, "leads/updatelead.html" , context)


# def createlead(request):
    # form = LeadForm()
    # if request.method == "POST":
    #     form = LeadForm(request.POST)
    #     if form.is_valid():
    #             first_name = form.cleaned_data['first_name']
    #             last_name = form.cleaned_data['last_name']
    #             age = form.cleaned_data['age']
    #             agent = Agent.objects.first()
    #             Lead.objects.create(
    #                 first_name=first_name,
    #                 last_name=last_name,
    #                 age=age,
    #                 agent=agent
    #             )
    # return redirect("/leads")
    # context = {
    #     "form": form
    # }
#     return render(request, "leads/createlead.html", context)