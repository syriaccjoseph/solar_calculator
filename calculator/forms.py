from django import forms

class AreaForm(forms.Form):
    area = forms.FloatField(required=True)