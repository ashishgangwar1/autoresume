from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import JobDescription
from .serializers import JDSerializer

class JobListView(APIView):
    def get(self, request):
        jobs = JobDescription.objects.all()
        serializer = JDSerializer(jobs, many=True)
        return Response(serializer.data)
