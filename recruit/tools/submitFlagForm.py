from django import forms
from captcha.fields import CaptchaField

class flagForm(forms.Form):
    chall = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    flag = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField()
