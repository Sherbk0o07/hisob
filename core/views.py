from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from  .models import Book
# Create your views here.

@api_view(['GET'])
def home(request):
    books = Book.objects.all()
    serializer = BookSerializer(books,many=True)

    return Response(serializer.data)


@api_view(['GET'])
def detail(request,id):
    book = Book.objects.get(id=id)
    serializer = BookDetailSerializer(book)

    return Response(serializer.data)


@api_view(['POST'])
def crate_book(request):
    serializer = BookDetailSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)