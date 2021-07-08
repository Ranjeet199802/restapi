from rest_framework import viewsets
from . import models
from . import serializers


class StudentViewset(viewsets.ModelViewSet):
    queryset = models.student.objects.all()
    serializer_class = serializers.StudentSerializer


class BooksViewset(viewsets.ModelViewSet):
    queryset = models.books.objects.all()
    serializer_class = serializers.BooksSerializer

# list(), retrive(), create(), update(), destroy() viewsets create these classes for us
