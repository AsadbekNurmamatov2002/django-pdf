from django.contrib import admin
from .models import Grops, Talaba, Talababaholash

# # Register your models here.

admin.site.register(Talaba)
admin.site.register(Talababaholash)
class TalabaInline(admin.TabularInline):
    model =Talababaholash
    raw_id_fields = ["grups"]

@admin.register(Grops)
class GropsAdmin(admin.ModelAdmin):
    list_display=['fan_nomi']
    inlines = [TalabaInline]