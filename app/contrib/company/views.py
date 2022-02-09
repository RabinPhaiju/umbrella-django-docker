from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CompanySerializer
from .models import Company


class CompanyView(APIView):
       def get(self,request,*args,**kwargs):
              data = Company.objects.all()
              serializer = CompanySerializer(data,many=True)
              return Response(serializer.data)
       
       def post(self,request,*args,**kwargs):
              serializer = CompanySerializer(data=request.data)
              if serializer.is_valid():
                     serializer.save()
                     return Response(serializer.data)
              return Response(serializer.errors)