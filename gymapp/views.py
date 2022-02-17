from django.shortcuts import render
from .models import Detail

# Create your views here.

def index(request):
    Details = Detail.objects.all()
    return render(request,'index.html',{'Details':Details})


def about(request):
    return render(request,'about.html')