from django.db import models
import time
# Create your models here.


def upload_to(instance, filename):
    stt = time.strftime("%Y%m%d", time.localtime())
    st1 = "04d" % (time.time()-int(time.time()))*10000
    return '/'.join(['cjdj', stt, st1+filename])


class user(models.Model):
    id = models.AutoField(primary_key=True)
    loginname = models.TextField(max_length=50)
    password = models.TextField(max_length=50)
#updatetime = models.DateTimeField()
#lastchapter = models.CharField(max_length=100)


class user_info(models.Model):
    name = models.TextField(max_length=50)
    tel = models.IntegerField(null=True,blank=True)
    cer = models.IntegerField(null=True,blank=True)
    uid = models.OneToOneField(user, on_delete=models.CASCADE)


class First_class(models.Model):
    class Meta:
        verbose_name_plural="一级目录"
    name = models.TextField(max_length=50,verbose_name="名称")
    about = models.TextField(max_length=500,null=True,blank=True)


class Second_class(models.Model):
    class Meta:
        verbose_name_plural="二级目录"
    name = models.TextField(max_length=50,verbose_name="名称")
    about = models.TextField(max_length=500,null=True,blank=True)
    fid = models.ForeignKey(First_class,on_delete=models.CASCADE,related_name="second")

class First_classInfo(models.Model):
    name = models.TextField(max_length=100,verbose_name="名称")
    context=models.TextField(max_length=1000,verbose_name="内容")
    fid = models.OneToOneField(First_class,on_delete=models.CASCADE)
    fj1= models.FileField(upload_to=upload_to,null=True,blank=True,verbose_name="附件1")
    fj1n =models.TextField(max_length=100,null=True,blank=True,verbose_name="附件1名称")
    fj2n =models.TextField(max_length=100,null=True,blank=True,verbose_name="附件2名称")
    fj3n =models.TextField(max_length=100,null=True,blank=True,verbose_name="附件3名称")
    fj4n =models.TextField(max_length=100,null=True,blank=True,verbose_name="附件4名称")
    fj2= models.FileField(upload_to=upload_to,null=True,blank=True,verbose_name="附件2")
    fj3= models.FileField(upload_to=upload_to,null=True,blank=True,verbose_name="附件3")
    fj4= models.FileField(upload_to=upload_to,null=True,blank=True,verbose_name="附件4")



class Second_classInfo(models.Model):
    name = models.TextField(max_length=100,verbose_name="名称")
    context=models.TextField(max_length=90000,null=True,blank=True,verbose_name="内容")
    fid = models.ForeignKey(Second_class,on_delete=models.CASCADE,related_name="secondinfo")
    fj1= models.FileField(upload_to=upload_to,verbose_name="附件1")
    fj1n =models.TextField(max_length=100,null=True,blank=True,verbose_name="附件1名称")
    fj2n =models.TextField(max_length=100,null=True,blank=True,verbose_name="附件2名称")
    fj3n =models.TextField(max_length=100,null=True,blank=True,verbose_name="附件3名称")
    fj4n =models.TextField(max_length=100,null=True,blank=True,verbose_name="附件4名称")
    fj2= models.FileField(upload_to=upload_to,null=True,blank=True,verbose_name="附件2")
    fj3= models.FileField(upload_to=upload_to,null=True,blank=True,verbose_name="附件3")
    fj4= models.FileField(upload_to=upload_to,null=True,blank=True,verbose_name="附件4")
    fj5n=models.TextField(max_length=100,null=True,blank=True,verbose_name="附件5名称")
    fj5= models.FileField(upload_to=upload_to,null=True,blank=True,verbose_name="附件5")
    fj6n=models.TextField(max_length=100,null=True,blank=True,verbose_name="附件6名称")
    fj6= models.FileField(upload_to=upload_to,null=True,blank=True,verbose_name="附件6")
    fj7n=models.TextField(max_length=100,null=True,blank=True,verbose_name="附件7名称")
    fj7= models.FileField(upload_to=upload_to,null=True,blank=True,verbose_name="附件7")





class Cjdj_info(models.Model):
    class Meta:
        verbose_name_plural="成交单价"
    id = models.AutoField(primary_key=True,verbose_name="ID")
    dizhi = models.TextField(max_length=500,verbose_name="地址")
    lx = models.TextField(max_length=500,verbose_name="类型")
    mianji = models.FloatField(verbose_name="面积")
    zongjia = models.FloatField(verbose_name="总价")
    dj = models.FloatField(verbose_name="单价")
    cjdate = models.DateField(verbose_name="成交日期")
    down = models.FileField(upload_to=upload_to,verbose_name="下载地址")
    area = models.TextField(max_length=500, null=True,blank=True,verbose_name="区")


def __str__(self):
    return self.text