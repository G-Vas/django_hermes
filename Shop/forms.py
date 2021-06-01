from django import forms
from .models import CallRequests
from phonenumber_field.formfields import PhoneNumberField


class CallRequestsForm(forms.ModelForm):
    # phone = PhoneNumberField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    class Meta:
        model = CallRequests
        fields = ['first_name', 'last_name', 'phone', 'question']



        widgets = {
            "phone": forms.NumberInput(attrs={'class': 'form-control',
                                              'placeholder': '380999999999'}),
            "first_name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "last_name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "question": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Вопрос',


            }),
            # "phone": PhoneNumberField(widget=forms.NumberInput, attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Прізвище'
            # })
            # "phone": forms.NumberInput(attrs={
            #     'placeholder': '+380'
            # })
        }
