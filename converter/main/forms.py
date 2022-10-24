from django import forms

def list_values():
    pass


class value_var(forms.Form):
    first_bar = forms.CharField(max_length=60, choices = list_values())



