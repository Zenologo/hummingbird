from django.db import models

class MyModelName(models.Model):
    """
    Merchant's model who representes all infos about merchant.
    """

    name = models.CharField(max_length=255, help_text="商家名称")
    web = models.URLField(help_text="商家网站") # Default length: 200
    tel = models.CharField(max_length=64, help_text="电话")
    country = models.CharField(max_length=64, help_text="国家")
    addresse = models.TextField(help_text="商家地址")

    def __str__(self):
        return self.name