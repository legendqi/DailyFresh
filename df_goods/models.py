from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class GoodsType(models.Model):
    """商品分类的模型类"""
    gtitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.gtitle

    class Meta:
        db_table = 'goodstype'

class GoodsInfo(models.Model):
    """商品的模型类"""
    gtitle = models.CharField(max_length=20)
    gprice = models.DecimalField(max_digits=5, decimal_places=2)
    gImage = models.ImageField(upload_to='df_goods')
    isDelete = models.BooleanField(default=False)
    gunit = models.CharField(max_length=20)
    gclick = models.IntegerField()
    gdescriptioni = models.CharField(max_length=200)
    gstore = models.IntegerField()
    gcontent = HTMLField()
    gtype = models.ForeignKey(GoodsType, on_delete=models.CASCADE)
    # gadv = models.BooleanField(default=False)

    class Meta:
        db_table = 'goodsinfo'