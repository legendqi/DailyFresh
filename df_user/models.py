from django.db import models

# Create your models here.


class ReceiveInfo(models.Model):
    username = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    postalCode = models.CharField(max_length=6)
    phoneNumber = models.CharField(max_length=11)

    class Meta:
        db_table = 'receiveinfo'


class UserInfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    receiveInformation = models.ForeignKey(ReceiveInfo, on_delete=models.CASCADE,)

    class Meta:
        db_table = 'userinfo'




