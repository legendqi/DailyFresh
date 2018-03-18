from django.db import models

# Create your models here.


class ReceiveInfo(models.Model):
    username = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=100, default='')
    postalCode = models.CharField(max_length=6, default='')
    phoneNumber = models.CharField(max_length=11, default='')
    # default,blank是Python层面的约束，不影响数据库表结构,不需要迁移

    class Meta:
        db_table = 'receiveinfo'


class UserInfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    receiveInformation = models.ForeignKey(ReceiveInfo, on_delete=models.CASCADE, default=1)

    class Meta:
        db_table = 'userinfo'




