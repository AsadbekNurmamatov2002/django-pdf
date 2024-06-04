from django.contrib import admin
from .models import Grops, Talaba, Talababaholash

# # Register your models here.

admin.site.register(Talaba)
admin.site.register(Talababaholash)
class TalabaInline(admin.TabularInline):
    model =Talababaholash
    readonly_fields=['bahosi']
    raw_id_fields = ["gruh"]

@admin.register(Grops)
class GropsAdmin(admin.ModelAdmin):
    list_display=['fan_nomi']
    readonly_fields=['fan_kredit']
    inlines = [TalabaInline]