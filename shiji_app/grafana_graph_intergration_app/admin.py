from django.contrib import admin
from .models import USDCurrencyModel, EurCurrencyModel, GBPCurrencyModel

# ! Registration of API models
admin.site.register(USDCurrencyModel)
admin.site.register(EurCurrencyModel)
admin.site.register(GBPCurrencyModel)