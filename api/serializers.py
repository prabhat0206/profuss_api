from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    product_name=serializers.CharField()
    category=serializers.CharField()
    description=serializers.CharField()
    image=serializers.ImageField()
    category_id=serializers.IntegerField()
    offer=serializers.IntegerField()
    price=serializers.IntegerField()
