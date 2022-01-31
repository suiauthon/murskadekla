from django.shortcuts import render

from .forms import PlantATreeForm
# Create your views here.

def plant_a_tree(request):
    args = {}
    form = PlantATreeForm()
    args["form"] = form
    return render(request, "plant_a_tree.html", args)
