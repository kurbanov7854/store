from django_filters import FilterSet, CharFilter
from .models import Product

class ProductFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains')
    class Meta:
        model = Product
        fields = ['name','type']
