from rest_framework import serializers

from core.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','price','publisher'] #['author']

    def to_representation(self, instance):
        total = super().to_representation(instance)

        total['publisher'] = instance.publisher.strftime("%Y-%m-%d")

        return total


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def to_representation(self, instance):
        total = super().to_representation(instance)

        total['publisher'] = instance.publisher.strftime("%Y-%m-%d")

        return total
