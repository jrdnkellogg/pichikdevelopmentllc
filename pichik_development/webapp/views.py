from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'webapp/index.html')

def firstlisting(request):
    return render(request, 'webapp/firstlisting.html')

def secondlisting(request):
    return render(request, 'webapp/secondlisting.html')

def thirdlisting(request):
    return render(request, 'webapp/thirdlisting.html')
