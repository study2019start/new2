from django.conf.urls import url
from . import views
from django.views.static import serve
from django.conf import settings


urlpatterns = [

    #url(r'^$', views.login, name='login'),
    #url(r'^login/$', views.login, name='login'),
    #url(r'^index/$', views.index, name='index'),
    url(r'^$', views.vtable, name='vtable'),
    url(r'^datalist/',views.getlist,name='getlist'),
    #url(r'^gtable$', views.cdatatable, name='cdatatable'),
    #url(r'down/(?P<id>\d+)', views.down, name='down'),
    url(r'^meida/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
]

app_name = 'websearch'