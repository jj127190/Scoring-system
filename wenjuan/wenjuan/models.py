# #-*-coding:utf-8-*-
# from django.db import models
# # Create your models here.
# class wenjuan_content(models.Model):
#     sub_line = models.CharField(verbose_name=_(u'产品线名称'), max_length=50,null=True, blank=True,default='')
#     jingli = models.CharField(verbose_name=(u'产品经理'), max_length=100,blank=True, null=True,default='')
#     qdzz = models.CharField(verbose_name=(u'前端组长'), max_length=50, blank=True, null=True,
#                                     default='')
#     qdxzcy = models.CharField(verbose_name=_(u'前端小组成员'), max_length=200, blank=True, null=True,
#                                     default='')
#     javazz = models.CharField(verbose_name=_(u'java组长'), max_length=50, blank=True, null=True, default='')
#     javaxzcy =  models.CharField(verbose_name=_(u'java小组成员'),max_length=200, blank=True, null=True,default='')
#     cszz = models.CharField(verbose_name=_(u'测试组长'), max_length=50, blank=True, null=True, default='')
#     csxzcy =  models.CharField(verbose_name=_(u'测试小组成员'),max_length=200, blank=True, null=True,default='')
#     last_content =  models.CharField(verbose_name=_(u'意愿调查'),max_length=50, blank=True, null=True,default='')
#     json_col = models.TextField(verbose_name=_(u'json序列化'), max_length=5000, null=True, editable=True)
#     auto_time = models.DateTimeField(auto_now_add=True, blank=True)
#     class Meta:
#         ordering = ['-auto_time']
#         verbose_name = u'问卷调查'
#
#         verbose_name_plural = verbose_name
#
#
#
# ##精简的
# # class wenjuan_info(models.Model):
# #     sub_line = models.CharField(verbose_name=_(u'产品线名称'), max_length=50,null=True, blank=True,default='')
# #     jingli_one = models.CharField(verbose_name=(u'产品经理'), max_length=50,blank=True, null=True,default='')
# #     jingli_two = models.CharField(verbose_name=(u'产品经理'), max_length=50, blank=True, null=True, default='')
# #
# #     qdzz = models.CharField(verbose_name=(u'前端组长'), max_length=50, blank=True, null=True,
# #                                     default='')
# #     qdxzcy = models.CharField(verbose_name=_(u'前端小组成员'), max_length=200, blank=True, null=True,
# #                                     default='')
# #
# #     javazz = models.CharField(verbose_name=_(u'java组长'), max_length=50, blank=True, null=True, default='')
# #
# #     javaxzcy =  models.CharField(verbose_name=_(u'java小组成员'),max_length=200, blank=True, null=True,default='')
# #
# #     cszz = models.CharField(verbose_name=_(u'测试组长'), max_length=50, blank=True, null=True, default='')
# #     csxzcy =  models.CharField(verbose_name=_(u'测试小组成员'),max_length=200, blank=True, null=True,default='')
# #     last_content =  models.CharField(verbose_name=_(u'意愿调查'),max_length=50, blank=True, null=True,default='')
# #     auto_time = models.DateTimeField(auto_now_add=True, blank=True)
# #     class Meta:
# #         ordering = ['-auto_time']
# #         verbose_name = u'问卷调查'
# #         verbose_name_plural = verbose_name