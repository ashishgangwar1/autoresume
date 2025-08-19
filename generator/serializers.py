from rest_framework import serializers

class ResumeGenerateSerializer(serializers.Serializer):
    profile_id = serializers.IntegerField()
    jd_text = serializers.CharField()
