from django.urls import path
from .views import Home, render_pdf_view, DetailView
app_name="pdfupload"
urlpatterns = [
    path("", Home, name='home'),
    path("detail/<str:id>/", DetailView, name="detail"),
    path('pdf/<str:pk>/',render_pdf_view ,name="pdf"),
]
