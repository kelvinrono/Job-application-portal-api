from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import UserProfile, Academics, Certifications, Experience
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=UserProfile
        fields ='__all__'

class AcademicsSerializer(serializers.ModelSerializer):

    class Meta:
        model=Academics
        fields ='__all__'

class CertificationSerializer(serializers.ModelSerializer):

    class Meta:
        model=Academics
        fields ='__all__'

class ExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model=Experience
        fields ='__all__'


