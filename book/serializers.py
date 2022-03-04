from rest_framework import serializers
from .models import Book, Author, Publisher, Category, BookItem, BookItemImage


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'biography', 'email', 'address']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'address']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    publisher = PublisherSerializer()
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['id', 'title', 'language', 'publicationDate', 'numberOfPages', 'category', 'author', 'publisher']


class BookItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookItemImage
        fields = ['id', 'image', 'index']


class BookItemSerializer(serializers.ModelSerializer):
    images = BookItemImageSerializer(many=True)
    book = BookSerializer()

    class Meta:
        model = BookItem
        fields = ['id', 'prices', 'description', 'barcode', 'header', 'discount', 'book', 'images']

