from django.shortcuts import render
from django.contrib import messages
from django import forms
from websearch.models import user,Cjdj_info
from django.forms import widgets
import os
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
# Create your views here.

class DateEncoder(json.JSONEncoder):  
    def default(self, obj):  
        if isinstance(obj, datetime.datetime):  
            return obj.strftime('%Y-%m-%d %H:%M:%S')  
        elif isinstance(obj, datetime.date):  
            return obj.strftime("%Y-%m-%d")  
        else:  
            return json.JSONEncoder.default(self, obj) 



def vtable(request):
    return render(request, 'websearch/table.html')


@csrf_exempt
def getlist(request):
    print(request.POST)
    dictt={}
    dic={}
    curr= request.POST.get('page') if request.POST.get('page')  else 1#第几页
    nums=request.POST.get('limit')  if  request.POST.get('limit') else 10 #一页多少个
    if  request.POST.get('dizhi') :
        dizhi=request.POST.get('dizhi')
        if dizhi:
            dic['dizhi__icontains']=dizhi
    if request.POST.get('areaq') :
        area=request.POST.get('areaq') 
        if area !="":
            dic['area']=area
    if request.POST.get('lx1') :
        lx=request.POST.get('lx1') 
        if lx !="":
            dic['lx']=lx
    if dic:
        result =  Cjdj_info.objects.filter(**dic).values()
    else:
        result =  Cjdj_info.objects.all().values()
    print(result)
    list_result = [entry for entry in result]
    p=Paginator(list_result ,int(nums))
    jishu=len(list_result )
    dictt['code']=0
    dictt['msg']=""
    dictt['count']=jishu
    try:
        page= p.page(int(curr))
    # todo: 注意捕获异常
    except PageNotAnInteger:
        # 如果请求的页数不是整数, 返回第一页。
        page = p.page(1).object_list
    except EmptyPage:
        # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
        page =p.page(p.num_pages).object_list
    except InvalidPage:
        # 如果请求的页数不存在, 重定向页面
        dictt['data']=""
        return HttpResponse(json.dumps(dictt,ensure_ascii=False),content_type="application/json,charset=utf-8")


    dictt['data']=page.object_list
    return HttpResponse(json.dumps(dictt,cls=DateEncoder,ensure_ascii=False),content_type="application/json,charset=utf-8")