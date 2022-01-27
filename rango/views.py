import rango
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #c3
    #return HttpResponse('Rango says hey there partner! <a href=\'/rango/about/\'>About</a>')
    #c4
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

#chapter3
def about(request):
    #c3
    #return HttpResponse('Rango says here is the about page. <a href=\'/rango/\'>Index</a>')
    #c4
    context_dict = {'myname': '2584092j, xiaowei jia'}
    return render(request, 'rango/about.html', context=context_dict)
