from django.urls import path
from .views import Home, render_pdf_view

urlpatterns = [
    path('', Home, name='home'),
    path('pdf/',render_pdf_view ,name="pdffile")
]
