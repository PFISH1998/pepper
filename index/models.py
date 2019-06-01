from django.db import models


# 舆情事件数据
class Event(models.Model):
    # 事件标题
    title = models.CharField(max_length=50, null=False)
    # 创建事件时间
    created_time = models.DateTimeField()
    # 备注或标记
    mark = models.CharField(max_length=50)
    # 关键词
    keyword = models.CharField(max_length=50)
    #yyl

    #lxy到此一游～
    #SCYg
