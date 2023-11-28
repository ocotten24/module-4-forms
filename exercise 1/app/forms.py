from django import forms

class ageInForm(forms.Form):
    birthyear = forms.IntegerField()
    endyear = forms.IntegerField()


class orderForm(forms.Form):
    burger = forms.IntegerField()
    fries = forms.IntegerField()
    drink = forms.IntegerField()