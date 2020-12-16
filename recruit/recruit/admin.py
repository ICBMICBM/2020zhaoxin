from django.contrib import admin
from recruit.models import user,signUp
from chall.models import flag

# Register your models here.
admin.site.register(user)
admin.site.register(flag)
admin.site.register(signUp)
