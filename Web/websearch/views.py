from django.shortcuts import render
from django.contrib import messages
from django import forms
from websearch.models import user,Cjdj_info,First_class,First_classInfo,Second_class,Second_classInfo
from django.forms import widgets
import os
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from django.http import StreamingHttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.conf import settings
from django.utils.encoding import escape_uri_path
from django.forms.models import model_to_dict
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
    fi=First_class.objects.all().values()
    fis=[a for a in fi]
    ss=[]
    for ff in fis:
        f=First_class.objects.get(id=ff['id'])
        ff['rows']=0
        if f.second.count()>0:
            ff['rows']=1
            ff['second']=[a for a in f.second.all().values()]
        ss.append(ff)
    ffs={'first1':ss}
    print(ss)
    return render(request, 'websearch/table.html',ffs)


def getlistmu(request):
    idn=request.POST.get("idn")
    r1 = Second_class.objects.filter(fid_id=idn).values()
  
    ss=[ r  for  r in r1]
    s1=json.dumps(ss, ensure_ascii=False)
    return HttpResponse(s1,content_type="application/json,charset=utf-8")



def file_iterator(file_path, chunk_size=512):
        """
        文件生成器,防止文件过大，导致内存溢出
        :param file_path: 文件绝对路径
        :param chunk_size: 块大小
        :return: 生成器
        """
        with open(file_path, mode='rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
@csrf_exempt
def getdo(request):
    print(request)
    fi=request.POST.get('vv')
    file_path=os.path.join(settings.MEDIA_ROOT,fi)
    print(file_path)
    if  os.path.isfile(file_path): 
        file_name=os.path.basename(file_path)
        print(file_name)
        try:
                # 设置响应头
                # StreamingHttpResponse将文件内容进行流式传输，数据量大可以用这个方法
            response = StreamingHttpResponse(file_iterator(file_path))
                # 以流的形式下载文件,这样可以实现任意格式的文件下载
            response['Content-Type'] = 'application/octet-stream'
                # Content-Disposition就是当用户想把请求所得的内容存为一个文件的时候提供一个默认的文件名
            response['Content-Disposition'] = 'attachment;filename="{0}"'.format(escape_uri_path(file_name))
        except:
            return HttpResponse("Sorry but Not Found the File")
            
        return response

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
    if request.POST.get('datestart') :
        ds=request.POST.get('datestart') 
        if ds !="":
            dic['cjdate__gte']=ds
    if request.POST.get('dateend') :
        de=request.POST.get('dateend') 
        if de !="":
            dic['cjdate__lte']=de
    if dic:
        result =  Cjdj_info.objects.filter(**dic).values()
    else:
        result =  Cjdj_info.objects.all().values()

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