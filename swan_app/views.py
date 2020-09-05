from django.shortcuts import render
from .models import Restaurants,FOOD

# Create your views here.

def index(request):
    return render(request, "index.html")
    