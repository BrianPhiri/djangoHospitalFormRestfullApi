from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.Serializer):
    class meta:
        model = Patient
        fields = ('firstname', 'lastname', 'email', 'city', 'address', 'phone', 'gender', 'age')