from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.db.models import Q
from .models import Talababaholash, Talaba, Grops

# Create your views here.
def render_pdf_view(request, pk):
    
    talababaholash = Talababaholash.objects.get(pk=pk)
    template_path = 'index.html'
    context={'talababoholash': talababaholash}
    response = HttpResponse(content_type='application/pdf')
    
    response['Content-Disposition'] = 'attachment; filename="baxolash.pdf"'
    
    template = get_template(template_path)
    html = template.render(context)
    
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def Home(request):
   grops=Grops.objects.all()
   return render(request, "hometo.html", {"grops":grops})

def Baholash(request, pk):
   talababaholash = Talababaholash.objects.get(pk=pk)
   return render(request, 'ditail.html', {})

def DetailView(request, id):
   grops=Grops.objects.get(id=id)
   talababaholash=grops.talababaholash_set.all()
   return render(request, "detail.html", {"talababaholash":talababaholash})