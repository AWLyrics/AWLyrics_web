from django import forms
class generateForm(forms.Form):
    name = forms.CharField(max_length=20)
    email= forms.CharField(max_length=20)
    message = forms.CharField(max_length=20)
