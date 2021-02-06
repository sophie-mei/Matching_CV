from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
#def search_index(request): 
    #return render(request, 'esearch1/accueil.html')

from django.shortcuts import render
from .es_call import esearch
# Create your views here.

def search_index(request):
    results = []
    nom_term = ""
    compétence_term = ""
    if request.GET.get('NOM') and request.GET.get('compétence'):
        nom_term = request.GET['NOM']
        compétence_term = request.GET['compétence']
    elif request.GET.get('NOM'):
        nom_term = request.GET['NOM']
    elif request.GET.get('compétence'):
        compétence_term = request.GET['compétence']
    search_term = nom_term or compétence_term
    results = esearch(NOM = nom_term, compétence=compétence_term)
    print(results)
    context = {'results': results, 'count': len(results), 'search_term':  search_term}
    return render(request,  'esearch1/accuiel.html',  context)

