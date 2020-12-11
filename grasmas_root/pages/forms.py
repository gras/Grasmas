from django import forms


class LampForm(forms.Form):
    class Meta:
        a = forms.CharField(max_length=30)