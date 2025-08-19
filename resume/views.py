from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Resume
from .serializers import ResumeSerializer

class ResumeListView(APIView):
    def get(self, request):
        resumes = Resume.objects.all()
        serializer = ResumeSerializer(resumes, many=True)
        return Response(serializer.data)
