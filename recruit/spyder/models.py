from django.db import models
from random import randint


def make_flag():
    dic = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ0123456789'
    code = 'spctf{'
    for i in range(5):
        code += dic[randint(0, len(dic) - 1)]
    code += '}'
    return code


class log(models.Model):
    def log_id(self):
        return self.id

    answer = models.IntegerField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    flag = models.CharField(default="NSS{SpiderCrawling}",max_length=12)


