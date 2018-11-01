from django.contrib import admin
from merchant.models import Merchant, MerchantCatalog, MerchantProduct

admin.site.register(Merchant)
admin.site.register(MerchantCatalog)
admin.site.register(MerchantProduct)
