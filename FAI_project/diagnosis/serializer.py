from .models import Diagnosis
from rest_framework import serializers

class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ['diag_id', 'user_id', 'diag_date', 'diag_image']