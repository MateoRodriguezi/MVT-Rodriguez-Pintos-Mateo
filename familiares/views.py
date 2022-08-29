from django.http import HttpResponse
from django.template import Template, Context, loader
from familiares.models import datos_familia

def listar_familia(request):
    queryset = datos_familia.objects.all()
    diccionario = {'datos': queryset}
    plantilla = loader.get_template('familia_list.html')
    documento_html = plantilla.render(diccionario)

    return HttpResponse(documento_html)