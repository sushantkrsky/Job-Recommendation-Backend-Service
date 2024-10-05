from rest_framework import serializers
from .models import UserProfile, JobPosting


class UserProfileSerializer(serializers.ModelSerializer):
    class PreferencesSerializer(serializers.Serializer):
        desired_roles = serializers.ListField(child=serializers.CharField())
        locations = serializers.ListField(child=serializers.CharField())
        job_type = serializers.CharField()

    preferences = PreferencesSerializer()

    class Meta:
        model = UserProfile
        fields = ['name', 'skills', 'experience_level', 'preferences']

class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = '__all__'  # Or specify individual fields if preferred
