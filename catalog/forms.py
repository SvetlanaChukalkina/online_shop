from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.constants import forbidden_list
from catalog.models import Product

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise ValidationError('Цена продукта не может быть отрицательной')
        return price

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name', '').lower()
        description = cleaned_data.get('description', '').lower()
        for word in forbidden_list:
            if word in name or word in description:
                self.add_error ('name', f'Имя или описание продукта не может содержать слово {word}')