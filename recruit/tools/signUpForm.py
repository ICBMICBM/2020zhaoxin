from django import forms
from captcha.fields import CaptchaField


class signUpForm(forms.Form):
    def clean_title(self):
        return self.cleaned_data['qq'].capitalize()

    sid = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    QQ = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="QQ")
    captcha = CaptchaField()
