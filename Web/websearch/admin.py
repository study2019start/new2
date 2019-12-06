from django.contrib import admin
from websearch.models import Cjdj_info

# Register your models here.
class Cjdjadmin(admin.ModelAdmin):
    list_display=('id','lx','dizhi','dj','cjdate')
    search_fields = ['dizhi']
admin.site.register(Cjdj_info,Cjdjadmin)