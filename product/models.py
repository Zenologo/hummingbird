from django.db import models
# from merchant.models import Merchant, MerchantCatalog

class Product(models.Model):
    """
    Product infos
    """
    # CURRENCY_PRODUCT = (
    #     ('EUR','欧元'),
    #     ('USD','美元'),
    #     ('GBP','英磅'),
    #     ('CNY','人民币'),
    # )
    
    # COUNTRY_LIST = (
    #     ('France', '法国'),
    #     ('China', '中国'),
    #     ('Germany', '德国' ),
    #     ('Italy', '意大利'),
    #     ('US', '美国'),
    #     ('UK', '英国'),
    # )

    name = models.CharField(verbose_name = '产品名', max_length = 255, help_text='产品名')
    chinese_name = models.CharField(verbose_name = '中文名称', max_length = 255, help_text='中文名称', blank=True)
    #merchant = models.ForeignKey('merchant.Merchant', verbose_name = '商家名称', on_delete = models.CASCADE, help_text = '商家名称')
    brand = models.ForeignKey('ProductBrand', verbose_name = '品牌名', on_delete = models.SET_NULL, help_text = '品牌名', null = True)
    description = models.TextField(verbose_name = '产品介绍', help_text='产品介绍', blank=True)
    specification = models.CharField(verbose_name = '产品规格', max_length = 16, help_text = '产品规格', blank=True)
    # created_time = models.DateTimeField(auto_now_add=True)
    
    # url = models.URLField(verbose_name='产品链接', help_text='产品链接', blank=True) # Default length: 200
    # price = models.DecimalField(max_digits = 18, verbose_name='价格',  decimal_places=2, help_text='价格', blank=True)
    # currency = models.CharField(verbose_name= '货币', max_length = 16, 
    #     choices = CURRENCY_PRODUCT, help_text = '货币', blank = True)
    # country = models.CharField(verbose_name= '国家', max_length = 32, 
    #     choices = COUNTRY_LIST, help_text = '商家所在国家', blank = True)

    def __str__(self):
        return self.name


class ProductBrand(models.Model):
    '''
    Brands infos
    '''
    
    COUNTRY_LIST = (
        ('France', '法国'),
        ('China', '中国'),
        ('Germany', '德国' ),
        ('Italy', '意大利'),
        ('US', '美国'),
        ('UK', '英国'),
    )

    name = models.CharField(verbose_name = '品牌名', max_length = 255, help_text='品牌名')
    description = models.TextField(verbose_name = '品牌介绍', help_text='品牌介绍', blank=True)
    url = models.URLField(verbose_name='品牌链接', help_text='品牌链接', blank=True) # Default length: 200
    # created_time = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.name