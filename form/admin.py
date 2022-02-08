from django.contrib import admin
from .models import Fabric, Fabricprop, EndUser , Material

# Register your models here.
admin.site.register(EndUser)
admin.site.register(Fabric)
admin.site.register(Fabricprop)
admin.site.register(Material)