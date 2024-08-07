from rest_framework import serializers
from .models import ShowDataModel


class ShowDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowDataModel
        fields = '__all__'

