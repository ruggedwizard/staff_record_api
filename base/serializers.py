from rest_framework import serializers
from base.models import StaffRecords

class StaffRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffRecords
        fields = '__all__'
        # fields = ['staff_id',]