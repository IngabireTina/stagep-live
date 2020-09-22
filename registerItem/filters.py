import django_filters
from .models import *


class StockFilter(django_filters.FilterSet):
    class Meta:
        model = Stock
        fields = ['code', 'name']


class ItemFilter(django_filters.FilterSet):
    class Meta:
        model = Item
        fields = ['address', 'person']


class SectorReportFilter(django_filters.FilterSet):
    class Meta:
        model = Item
        fields = ['person', 'device']


# class AssignDevice(django_filters.FilterSet):
#     class Meta:
#         model = Item
#         fields = ['device']
