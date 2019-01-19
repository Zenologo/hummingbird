from django.db import models
from product.models import ProductBrand, Product
from datetime import datetime

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


    type = models.CharField(verbose_name = '商家类型', max_length = 5, choices = MERCHANT_TYPE,
        default = WEB, help_text = '商家类型', blank=True
    )

    def __str__(self):
        return self.name


class MerchantCatalog(models.Model):
    """
    Website's catalog.
    The catalog is a range of products and a task for Gecko.
    """
    # name = models.CharField(verbose_name = '品牌名', max_length = 255, help_text='品牌名')
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name = '品牌名', blank = True, max_length = 255, help_text = '品牌名')
    merchant = models.ForeignKey(Merchant, verbose_name = '商家名称', on_delete = models.CASCADE, null = True, help_text = '商家名称')
    brand = models.ForeignKey(ProductBrand, on_delete = models.CASCADE, null = True, help_text = '品牌名')
    
    url = models.URLField(verbose_name='品牌链接', help_text='品牌链接', blank=True) # Default length: 200
    description = models.TextField(verbose_name = '品牌介绍', help_text='品牌介绍', blank=True)

    def __str__(self):
        return "catalog_" + str(self.id) + "_" + str(self.brand)


class MerchantProduct(models.Model):
    id = models.AutoField(primary_key=True)
    merchant = models.ForeignKey(Merchant, verbose_name = 'Merchant', on_delete = models.CASCADE, null = True, help_text = '商家名称')
    brand = models.ForeignKey(MerchantCatalog, verbose_name = 'Brand', on_delete = models.CASCADE, null = True, help_text = '品牌名')
    product = models.ForeignKey(Product, on_delete = models.CASCADE, null = True, help_text='产品名')
    
    # chinese_name = models.CharField(verbose_name = 'Chinese name', max_length = 255, help_text='中文名称', blank=True)
    # url = models.URLField(verbose_name='URL', help_text='产品目录链接', blank=True) # Default length: 200
    # price = models.DecimalField(max_digits = 18, verbose_name='Price',  decimal_places=2, help_text='价格', blank=True)
    # short_description = models.TextField(verbose_name = 'Short description', help_text='产品简介', blank=True) 
    # description = models.TextField(verbose_name = 'Description', help_text='产品介绍', blank=True)
    # specification = models.CharField(verbose_name = 'Specification', max_length = 16, help_text = '产品规格', blank=True)
    # date = models.DateTimeField(verbose_name = 'Last modified time', default = datetime.now, blank = True, help_text = '更新时间')
    
    def __str__(self):
        return "product_" + str(self.id) + "_" + str(self.product)


class PriceMonitor(models.Model):
    id = models.AutoField(primary_key=True)
    merchant_product = models.ForeignKey(MerchantProduct, on_delete = models.CASCADE, null = True, help_text='产品名')
    url = models.URLField(verbose_name='URL', help_text='产品目录链接', blank=True) # Default length: 200
    price = models.DecimalField(max_digits = 18, verbose_name='Price',  decimal_places=2, help_text='价格', blank=True)
    short_description = models.TextField(verbose_name = 'Short description', help_text='产品简介', blank=True) 
    description = models.TextField(verbose_name = 'Description', help_text='产品介绍', blank=True)
    specification = models.CharField(verbose_name = 'Specification', max_length = 16, help_text = '产品规格', blank=True)
    date = models.DateTimeField(verbose_name = 'Last modified time', default = datetime.now, blank = True, help_text = '更新时间')
    
    def __str__(self):
        return "product_" + str(self.id) + "_" + str(self.merchant_product)
