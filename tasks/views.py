from django.shortcuts import render 
from django.http import HttpResponse

intro = "Below my favourite some books"
books = ["Bangla", "English", "Math", "Physices", "Chemstry"]
# Create your views here.
def index(request):
    return render(request, "tasks/add.html",{
        "intro" : intro,
        "tasks" : books,
    })

def added (request):
    return render(request, "tasks/added.html",{
        
    })