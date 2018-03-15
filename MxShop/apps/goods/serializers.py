# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import Goods, GoodsCategory


class CategorySerializer3(serializers.ModelSerializer):
    """Goods category serializer 3
    """
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class CategorySerializer2(serializers.ModelSerializer):
    """Goods category serializer 2
    """
    sub_cat = CategorySerializer3(many=True) # do not forget set many to True
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """Goods category serializer
    """
    sub_cat = CategorySerializer2(many=True) # do not forget set many to True
    class Meta:
        model = GoodsCategory
        fields = '__all__'


## Method 1
# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True, max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()
#     # others...
#
#     def create(self, validated_data):
#         return Goods.objects.create(**validated_data)


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Goods
        # fields = ('name', 'click_num', 'market_price', 'add_time')
        fields = "__all__"

