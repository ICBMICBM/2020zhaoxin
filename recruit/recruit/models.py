from django.db import models

class user(models.Model):

    def id(self):
        return self.id()

    userPassword = models.CharField(max_length=512, null=False)  # 用户密码密文
    userEmail = models.EmailField(null=False)  # 用户邮箱
    userQQ = models.IntegerField(null=True)  # 用户qq
    userFlagSum = models.IntegerField(default=0, null=False)  # 用户flag数量
    userLatestFlag = models.CharField(max_length=32, null=False, default="NSS{W3LCOM3_TO_SWPU}")  # 用户最新flag
    solved = models.CharField(max_length=512, null=True, default='{}')  # 用户已完成的题目


class signUp(models.Model):

    def id(self):
        return self.id()

    userEmail = models.EmailField(null=False)
    userPassword = userPassword = models.CharField(max_length=512, null=False)
    userQQ = models.IntegerField(null=False)
    userFlagCount = models.IntegerField(default=0, null=False)
    solved = models.CharField(max_length=512, null=True, default='{}')
    sid = models.IntegerField(null=False)
    name = models.CharField(max_length=16, null=False)

# Create your models here.
