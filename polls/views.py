from django.shortcuts import render
from django.http import HttpResponse


def index(request):     
    #return HttpResponse("Emir Elçi'nin Kişisel Sayfası \n Meraba")
    return render(request,'style.html')
