from rest_framework import serializers

class TeacherSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    phone_number = serializers.IntegerField()
    city = serializers.CharField(max_length=50)