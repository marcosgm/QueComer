'''
Created on 12/09/2011

@author: marcosgarciamarti
'''
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    # ...
    if True:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    else:
        return HttpResponse('<h1>INDEX Page was found</h1>')
    
    
def detail(request):
    # ...
    if True:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    else:
        return HttpResponse('<h1>DETAIL Page was found</h1>')