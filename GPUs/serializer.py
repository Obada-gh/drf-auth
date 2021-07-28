from rest_framework import serializers
from .models import rtx
class GpusSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'description', 'created_at', 'company')
        model = rtx
        