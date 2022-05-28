
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Academics, UserProfile, Certifications, Experience
from rest_framework.response import Response
from .serializers import AcademicsSerializer, UserProfileSerializer, CertificationSerializer, ExperienceSerializer
from rest_framework import status
# Create your views here.

class UserProfileView(APIView):
    def get(self, request, format=None):
        profile = UserProfile.objects.all()
        serializer = UserProfileSerializer(profile, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer=UserProfileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class AcademicView(APIView):
#     def get(self, request, format=None):
#         academics=Academics.objects.all()
#         serializer=AcademicsSerializer(academics, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer=AcademicsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class CertificationView(APIView):
#     def get(self, request, format=None):
#         certifications=Certifications.objects.all()
#         serializer=CertificationSerializer(certifications, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer=CertificationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ExperienceView(APIView):
#     def get(self, request, format=None):
#         experience=Experience.objects.all()
#         serializer=ExperienceSerializer(experience, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer=ExperienceSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)



        

