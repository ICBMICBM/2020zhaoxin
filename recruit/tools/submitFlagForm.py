from django import forms
from captcha.fields import CaptchaField

class flagForm(forms.Form):
    flag = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField()
