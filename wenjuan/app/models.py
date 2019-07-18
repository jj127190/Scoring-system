#-*-coding:utf-8-*-
from django.db import models

# Create your models here.
class wenjuan_content(models.Model):
    sub_line = models.CharField(verbose_name=(u'产品线名称'), max_length=500,null=True, blank=True,default='')
    jingli = models.CharField(verbose_name=(u'产品经理'), max_length=500,blank=True, null=True,default='')
    qdzz = models.CharField(verbose_name=(u'前端组长'), max_length=500, blank=True, null=True,
                                    default='')
    qdxzcy = models.CharField(verbose_name=(u'前端小组成员'), max_length=2000, blank=True, null=True,
                                    default='')
    javazz = models.CharField(verbose_name=(u'java组长'), max_length=500, blank=True, null=True, default='')
    javaxzcy =  models.CharField(verbose_name=(u'java小组成员'),max_length=2000, blank=True, null=True,default='')
    cszz = models.CharField(verbose_name=(u'测试组长'), max_length=500, blank=True, null=True, default='')
    csxzcy =  models.CharField(verbose_name=(u'测试小组成员'),max_length=2000, blank=True, null=True,default='')
    last_content =  models.CharField(verbose_name=(u'意愿调查'),max_length=500, blank=True, null=True,default='')
    json_col = models.TextField(verbose_name=(u'json序列化'), max_length=5000, null=True, editable=True)

    auto_time = models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
        ordering = ['-auto_time']
        verbose_name = u'问卷调查'
        verbose_name_plural = verbose_name
        permissions = (
            ("wenjuan_del", "问卷调查删除"),
            ("wenjuan_update", "问卷调查更新"),
            ("wenjuan_add", "问卷调查增加"),
        )
