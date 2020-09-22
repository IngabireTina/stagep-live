from django.forms import ModelForm
from .models import Item
from .models import Stock


class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['device'].queryset = Stock.objects.exclude(availability='Given')
        self.fields['device'].widget.attrs['readonly'] = True


class ReportItemForm(ModelForm):

    class Meta:
        model = Item
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ReportItemForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['person'].widget.attrs['readonly'] = True
            self.fields['device'].widget.attrs['readonly'] = True
            self.fields['title'].widget.attrs['readonly'] = True
            self.fields['address'].widget.attrs['readonly'] = True

    def clean_device(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.device
        else:
            return self.cleaned_data.get('device', None)


