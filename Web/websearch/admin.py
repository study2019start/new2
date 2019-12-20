from django.contrib import admin
from websearch.models import Cjdj_info,First_class,First_classInfo,Second_class,Second_classInfo

# Register your models here.
class Cjdjadmin(admin.ModelAdmin):
    list_display=('id','lx','dizhi','dj','cjdate')
    search_fields = ['dizhi']

class Second_classM(admin.StackedInline):
    model=Second_class

class First_admin(admin.ModelAdmin):
    list_display=('name',)
    search_fields=['name']
    inlines=[Second_classM,]



admin.site.register(Cjdj_info,Cjdjadmin)
admin.site.register(First_class,First_admin)
admin.site.register(First_classInfo)
admin.site.register(Second_class)
admin.site.register(Second_classInfo)