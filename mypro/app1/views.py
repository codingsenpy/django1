from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("i am from app1")

def demo(request):
    return HttpResponse("fbwydajhw")