from django.db import models

class user(models.Model):

    def id(self):
        return self.id()

    userPassword = models.CharField(max_length=512,null=False)  # 用户密码密文
    userEmail = models.EmailField(null=False)  # 用户邮箱
    userQQ = models.IntegerField(null=True)  # 用户qq
    userFlagSum = models.IntegerField(default=0,null=False)  # 用户flag数量
    userLatestFlag = models.CharField(max_length=32,null=False,default="NSS{W3LCOM3_TO_SWPU}")  # 用户最新flag

# Create your models here.
