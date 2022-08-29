from django.http import HttpResponse
from django.template import Template, Context, loader
from familiares.models import Datos

def listar_familia(request):
    queryset = Datos.objects.all()
    diccionario = {'familiares': queryset}
    plantilla = loader.get_template('familia_list.html')
    documento_html = plantilla.render(diccionario)

    return HttpResponse(documento_html)