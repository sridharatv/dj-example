from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse ("<font face=\"verdana\" color=\"red\" size=20>"
#                          "This is from my first Django App</font>")
#
#

def index(request):
	mydict = {'tmpl_ins':"This is from index template views from webapp/index.html"}
	return render (request, 'webapp/index.html',context=mydict)

