from rest_framework import serializers
class ProductsSerializer(serializers.Serializer):
    brand = serializers.CharField(max_length = 80)
    productGroup = serializers.CharField(max_length = 70)
    title = serializers.CharField(max_length = 60)
    price = serializers.IntegerField()