from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse ("Rango says hey there partner here is the link! <br/> <a href = '/rango/about/'> About</a>")
    
def about(request):
    return HttpResponse ("Rango says is the about page.  <a href='/rango/'> Index</a>")

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')
