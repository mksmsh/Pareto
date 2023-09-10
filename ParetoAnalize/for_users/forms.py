from django import forms
from .models import Shop, Sale
from for_admin.models import MarketPlace, ModelWork, MethodofExport, TariffTranslate


class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField()


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['shop']


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['nameSH', 'mp', 'md', 'moe', 'tt']


class ShopSelectionForm(forms.Form):
    shop = forms.ModelChoiceField(queryset=None)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['shop'].queryset = Shop.objects.filter(creator=user)
        self.fields['shop'].label = 'Выберите ваш магазин'  # Добавьте подходящее описание

    class Meta:
        model = Shop