from django import forms


class IdForm(forms.Form):
    contract_id = forms.IntegerField()
