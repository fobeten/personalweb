from django.http import HttpResponse
from django.shortcuts import render

def home_page_view(request):
    context = {
        "owner" : "Mema"
    }
    return render(request, "pages/index.html", context)

def about_page_view(request):
    context = {
        "name" : "Klaus",
        "class" : "not your class",
    }
    return render(request, "pages/about.html",context)
