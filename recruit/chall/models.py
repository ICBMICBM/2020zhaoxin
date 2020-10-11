from django.db import models

class flag(models.Model):

    def id(self):
        return self.id

    flag = models.CharField(max_length=64,null=False,default="NSS{fake_flag}")
    chall = models.IntegerField(null=False)