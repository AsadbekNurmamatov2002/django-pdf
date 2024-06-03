from django.contrib import admin
from django.urls import path, include
admin.site.site_header="Talaba Baholash"
admin.site.site_title ="Talaba"
admin.site.index_title="Hush Kelibsiz"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pdfupload.urls')),
]
