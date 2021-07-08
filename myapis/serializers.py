from rest_framework import serializers
from .models import student, books


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = books
        fields = '__all__'
