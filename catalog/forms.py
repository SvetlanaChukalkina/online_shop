from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product
from config.settings import FORBIDDEN_LIST


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
        price = self.cleaned_data.get('price', 0)
        if price <= 0:
            raise ValidationError('Цена продукта не может быть отрицательной')
        return price

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        for word in FORBIDDEN_LIST:
            if word in name.lower():
                raise ValidationError(f'Имя продукта не может содержать слово {word}')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        for word in FORBIDDEN_LIST:
            if word in description.lower():
                raise ValidationError(f'Описание продукта не может содержать слово {word}')
        return description
