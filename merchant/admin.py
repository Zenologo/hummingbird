from django.contrib import admin
from merchant.models import Merchant, MerchantCatalog, MerchantProduct, PriceMonitor

admin.site.register(Merchant)
admin.site.register(MerchantCatalog)
admin.site.register(MerchantProduct)
admin.site.register(PriceMonitor)
