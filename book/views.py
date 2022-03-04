from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Book, BookItem
from .serializers import BookSerializer, BookItemSerializer
from rest_framework_simplejwt.backends import TokenBackend
# Create your views here.


class BookListAPIView(APIView):
    def get(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        data = {'token': token}
        valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
        user = valid_data['user']
        print(user)
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BookDetailAPIView(APIView):

    def get(self, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = JSONParser().parse(request)
        serializer = BookSerializer(book, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class BookItemListAPIView(APIView):

    def get(self, request):
        book_items = BookItem.objects.all()
        serializer = BookItemSerializer(book_items, many=True)
        return Response(serializer.data)



class BookItemDetailAPIView(APIView):

    def get(self, pk):
        try:
            book_item = BookItem.objects.get(pk=pk)
        except BookItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookItemSerializer(book_item)
        return Response(serializer.data)
