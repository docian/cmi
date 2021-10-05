from rest_framework import serializers
from .models import *

class PacientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacient
        fields = '__all__'

class TimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTable
        fields = '__all__'