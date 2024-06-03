from django.contrib import admin
from .models import Talaba, Teachers, KafidraMudir, Talababaholash, Fakultet, Fan, Yunalish, Grops

# Register your models here.

admin.site.register(Talaba)
admin.site.register(KafidraMudir)
admin.site.register(Teachers)
admin.site.register(Fakultet)
admin.site.register(Talababaholash)
# @admin.register(Talababaholash)
class TalabaInline(admin.TabularInline):
    model =Talababaholash
    raw_id_fields = ["grups"]

@admin.register(Grops)
class GropsAdmin(admin.ModelAdmin):
    list_display=['name']
    inlines = [TalabaInline]
admin.site.register(Fan)
admin.site.register(Yunalish)

# date_hierarchy = 'added_on'