from django import forms
from orders.models import Order

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int,)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']

        widgets = {
            "first_name": forms.TextInput(attrs={
                'class': 'form-first-name',
                'placeholder': 'Имя'
            }),
            "last_name": forms.TextInput(attrs={
                'class': 'form-first-name',
                'placeholder': 'Фамилия'
            }),
            "email": forms.EmailInput(attrs={
                    'class': 'form-first-name',
                    'placeholder': 'Электронная почта'
                }
            ),
            "postal_code": forms.NumberInput(attrs={
                'class': 'form-first-name',
                'placeholder': 'Почтовый индекс'
            }),
            "address": forms.TextInput(attrs={
                'class': 'form-first-name',
                'placeholder': 'Адрес'
            }),
            "city": forms.TextInput(attrs={
                'class': 'form-first-name',
                'placeholder': 'Город'
            }),
            }
