from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ResumeGenerateSerializer

class ResumeGenerateView(APIView):
    def post(self, request):
        serializer = ResumeGenerateSerializer(data=request.data)
        if serializer.is_valid():
            # Generate logic (we can add later)
            return Response({"message": "Resume generation logic pending"})
        return Response(serializer.errors, status=400)
