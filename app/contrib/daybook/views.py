from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DaybookSerializer
from .models import Daybook


class DaybookView(APIView):
       def get(self,request,*args,**kwargs):
              data = Daybook.objects.all()
              serializer = DaybookSerializer(data,many=True)
              return Response(serializer.data)
       
       def post(self,request,*args,**kwargs):
              serializer = DaybookSerializer(data=request.data)
              if serializer.is_valid():
                     serializer.save()
                     return Response(serializer.data)
              return Response(serializer.errors)