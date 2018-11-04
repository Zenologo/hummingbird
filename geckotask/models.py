from django.db import models
from merchant.models import Merchant

class GeckoTask(models.Model):
    '''
    Gecko's tasks. 
    '''
    
    name = models.CharField(verbose_name = '任务名', max_length = 255, help_text='任务名')
    url = models.URLField(verbose_name='任务链接', help_text='任务链接', blank=True) # Default length: 200
    merchant = models.ForeignKey('merchant.Merchant', verbose_name = '商家名称', on_delete = models.CASCADE, help_text = '商家名称')
    description = models.TextField(verbose_name = '任务介绍', help_text='任务介绍', blank=True)
    last_modyfied_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Parser(models.Model):
    '''
    Exprestion and step config.
    '''
    EXPRESSTION_TYPE = (
        ('XPath', 'XPath'),
        ('CSS', 'CSS'),
        ('RG', 'Regular Expression' ),
    )

    name = models.CharField(verbose_name = '表达式名称', max_length = 255, help_text='表达式名称')
    gecko_task = models.ForeignKey('GeckoTask', verbose_name = 'Gecko任务', on_delete = models.CASCADE, help_text = 'Gecko任务')
    type = models.CharField(verbose_name = '表达式类型', max_length = 20 , choices = EXPRESSTION_TYPE,
        default = 'XPath', help_text = '表达式类型', blank=True)
    active = models.BooleanField(default=1)
    order = models.PositiveIntegerField(default = 0, verbose_name = '运行顺序', help_text = '顺序是由小到大排序')

    def __str__(self):
        return self.name