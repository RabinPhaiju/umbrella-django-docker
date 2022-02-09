from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PartnerSerializer
from .models import Partner


class PartnerView(APIView):
       def get(self,request,*args,**kwargs):
              data = Partner.objects.all()
              serializer = PartnerSerializer(data,many=True)
              return Response(serializer.data)
       
       def post(self,request,*args,**kwargs):
              serializer = PartnerSerializer(data=request.data)
              if serializer.is_valid():
                     serializer.save()
                     return Response(serializer.data)
              return Response(serializer.errors)