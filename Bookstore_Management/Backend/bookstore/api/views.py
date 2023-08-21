from .models import BookStoreModel
from api.serializers import BookStoreSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BookListView(APIView):
    """
    List all books, or create a new book.
    """
    def get(self, request, format=None):
        model = BookStoreModel.objects.all()
        serializer = BookStoreSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookStoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)# create kora
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)# kothao vul ase
