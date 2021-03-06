# -*- coding: utf-8 -*-

import django_filters
from .models import Goods


class GoodsFilter(django_filters.FilterSet):
    """商品过滤类
    """
    price_min = django_filters.NumberFilter(name='shop_price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(name='shop_price', lookup_expr='lte')


    class Meta:
        model = Goods
        fields = ['price_min', 'price_max']