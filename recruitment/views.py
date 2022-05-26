from mmap import MADV_NOSYNC
from re import U
from django.shortcuts import render
from rest_framework.views import APIView
from .models import UserProfile
from rest_framework.response import Response
from .serializers import UserProfileSerializer
from rest_framework import status
# Create your views here.

class UserProfileView(APIView):
    def get(self, request, format=None):
        profile = UserProfile.objects.all()
        serializer = UserProfileSerializer(profile, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer=UserProfileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



