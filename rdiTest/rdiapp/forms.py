from django import forms

from .enums import Role

class RoleForm(forms.Form):
    role = forms.ChoiceField(choices=[(role.name, role.value) for role in Role])