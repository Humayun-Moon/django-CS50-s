from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.

def index(request):
    intro = "My life line which is my all Favourite Person"
    favourite = ["Allah", "Prophet(SA)", "Parants", "Mylife", "Help to Others"]
    return render(request, "first/index.html",{
        "intro" : intro,
        "favourite" : favourite
    })