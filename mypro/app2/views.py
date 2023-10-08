from django.shortcuts import render,HttpResponse

# Create your views here.
def s(request):
    return HttpResponse("i am from app2")
