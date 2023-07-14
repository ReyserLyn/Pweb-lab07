from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from datetime import datetime

from .utils import render_to_pdf 

class GeneratePDF(View): 
    def get(self, request, *args, **kwargs): 
        template = get_template('invoice.html') 
        context = { 
            "invoice_id": 5621, 
            "customer_name": "Reyser Zapata", 
            "amount": 1899.99, 
            "today": datetime.now(), 
        } 
        
        html = template.render(context) 
        pdf = render_to_pdf('invoice.html', context) 

        if pdf: 
            response = HttpResponse(pdf, content_type='application/pdf') 
            filename = "Invoice_%s.pdf" %("document") 
            content = "inline; filename='%s'" %(filename) 
            download = request.GET.get("download") 
            if download: 
                content = "attachment; filename='%s'" %(filename) 
            response['Content-Disposition'] = content 
            return response 
        return HttpResponse("Not found")