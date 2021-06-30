from django.shortcuts import render

# Create your views here.

#para que isso funcione, e preciso definilo no arquivo urls.py, dentro da polls
def index(request):
	return HttpResponse('hello word, this is my fist view')