from django.shortcuts import render

# Create your views here.
def index(request): 
    return render(request, "resort/index.html")

def about(request): 
    return render(request, "resort/about.html")

def contact(request): 
    return render(request, "resort/contact.html")


def dining(request): 
    return render(request, "resort/dining.html")

def conference(request): 
    return render(request, "resort/conference.html")

def accommodation(request): 
    return render(request, "resort/accommodation.html")


def reservation(request): 
    return render(request, "resort/reservation.html") 

def gallery(request): 
    return render(request, "resort/gallery.html")