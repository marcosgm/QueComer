'''
Created on 12/09/2011

@author: marcosgarciamarti
'''
from django.http import HttpResponse, HttpResponseNotFound, Http404
from quecomer.models import Plato
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.forms.models import modelformset_factory

def index(request):
    platos = Plato.objects.all()
    t = loader.get_template('main.html')
    c = Context({
        'lista_platos': platos,
    })
    return HttpResponse(t.render(c))

def detalle_plato(request, idplato):
    p = get_object_or_404(Plato,pk=idplato)
    return render_to_response('detalle_plato.html', {'detalle_plato': p},   context_instance=RequestContext(request))
def edit_plato(request, idplato):
    PlatoFormSet = modelformset_factory(Plato)
    if request.method=='POST':
        formset = PlatoFormSet (request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
    else:
        formset = PlatoFormSet()
        
    return render_to_response("manage_authors.html",{"formset":formset,})