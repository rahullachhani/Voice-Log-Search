from django import forms

class NameForm(forms.Form):
    file_names = forms.CharField(label='pic');