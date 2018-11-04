from django.db import models

class Merchant(models.Model):
    '''
    Merchant's model who representes all infos about merchant.
    '''

    WEB = 'Web'
    STORE = 'Store'
    MERCHANT_TYPE = (
        (WEB, WEB),
        (STORE, STORE)
    )

    COUNTRY_LIST = (
        ('France', '法国'),
        ('China', '中国'),
        ('Germany', '德国' ),
        ('Italy', '意大利'),
        ('US', '美国'),
        ('UK', '英国'),
    )

    name = models.CharField(verbose_name = '商家名称', max_length = 255, help_text = '商家名称')
    url = models.URLField(verbose_name = '网站', help_text = '商家网站', blank=True) # Default length: 200
    tel = models.CharField(verbose_name = '电话', max_length = 16, help_text = '商家电话', blank=True)
    country = models.CharField(verbose_name= '国家', max_length = 32, 
        choices = COUNTRY_LIST, help_text = '商家所在国家', blank = True)
    addresse = models.TextField(verbose_name = '地址', help_text = '商家地址', blank=True)
    last_modyfied_time = models.DateTimeField(auto_now_add=True)


    type = models.CharField(verbose_name = '商家类型', max_length = 5, choices = MERCHANT_TYPE,
        default = WEB, help_text = '商家类型', blank=True
    )

    def __str__(self):
        return self.name


class MerchantCatalog(models.Model):
    '''
    Website's catalog.
    The catalog is a range of products and a task for Gecko.
    '''
    
    name = models.CharField(verbose_name = '品牌名', max_length = 255, help_text='品牌名')
    url = models.URLField(verbose_name='品牌链接', help_text='品牌链接', blank=True) # Default length: 200
    merchant = models.ForeignKey('Merchant', verbose_name = '商家名称', on_delete = models.CASCADE, help_text = '商家名称')
    description = models.TextField(verbose_name = '品牌介绍', help_text='品牌介绍', blank=True)
    last_modyfied_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class MerchantProduct(models.Model):
    '''
    All merchant's products.
    '''

    name = models.CharField(verbose_name = '产品名', max_length = 255, help_text='产品名')
    chinese_name = models.CharField(verbose_name = '中文名称', max_length = 255, help_text='中文名称', blank=True)
    url = models.URLField(verbose_name='目录链接', help_text='产品目录链接', blank=True) # Default length: 200
    price = models.DecimalField(max_digits = 18, verbose_name='价格',  decimal_places=2, help_text='价格', blank=True)
    description = models.TextField(verbose_name = '产品介绍', help_text='产品介绍', blank=True)
    specification = models.CharField(verbose_name = '产品规格', max_length = 16, help_text = '产品规格', blank=True)
    last_modyfied_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name