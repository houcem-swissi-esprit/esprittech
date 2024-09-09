from django import forms

class UserRegisterForm(forms.Form):
    role = forms.ChoiceField()