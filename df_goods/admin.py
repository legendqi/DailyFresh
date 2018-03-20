from django.contrib import admin
from .models import *
# Register your models here.


class GoodsTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'gtitle']


class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'gtitle', 'gprice', 'gImage', 'isDelete', 'gunit', 'gclick', 'gdescriptioni', 'gstore'
                    , 'gcontent', 'gtype']
    list_per_page = 10


admin.site.register(GoodsType, GoodsTypeAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)