from django.contrib import admin
from .models import Director, AssociateDir, Manager, OperatorsKTZ, OperatorsElec, Crawler, Electric

admin.site.register(Director)
admin.site.register(AssociateDir)
admin.site.register(Manager)
admin.site.register(OperatorsKTZ)
admin.site.register(OperatorsElec)
admin.site.register(Crawler)
admin.site.register(Electric)
