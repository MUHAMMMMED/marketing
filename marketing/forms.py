
from django import forms
from marketing.models import *

class CallUsForm(forms.ModelForm):
    class Meta:
        model = CallUs
        fields = '__all__'
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-input w-input', 'maxlength': '256'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-input w-input', 'maxlength': '256'}),
            'Description': forms.Textarea(attrs={'class': 'form-input form-textarea w-input', 'maxlength': '5000'}),
        }
