# from django.shortcuts import render
# import os
# from django.conf import settings
# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa
# from django.contrib.staticfiles import finders
# from django.db.models import Q
# from .models import Talababaholash, Talaba, Grops, Fan

# # Create your views here.
# def render_pdf_view(request, pk):
#     grops=Grops.objects.get(pk=pk)
#     fans = grops.fan.all()
#     talababaholash = Talababaholash.objects.filter(Q(fan__in=fans) & Q(grups=grops))
#     template_path = 'index.html'
#     context={'talababoholash': talababaholash, "grops":grops}
#     response = HttpResponse(content_type='application/pdf')
    
#     response['Content-Disposition'] = 'attachment; filename="baxolash.pdf"'
    
#     template = get_template(template_path)
#     html = template.render(context)
    
#     pisa_status = pisa.CreatePDF(
#        html, dest=response)
#     if pisa_status.err:
#        return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response

# def Home(request, id):
#    # grops=Grops.objects.get(pk=id)
#    # fans = grops.fan.all()
#    # talababaholash = Talababaholash.objects.filter(Q(fan__in=fans) & Q(grups=grops))
#    return render(request, "home.html", {'talababoholash': talababaholash, "grops":grops})

# def Baholash(request, pk):
#    talababaholash = Talababaholash.objects.get(pk=pk)
#    return render(request, 'ditail.html', {})