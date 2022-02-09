from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Daybook_typeSerializer
from .models import Daybook_type


class Daybook_typeView(APIView):
       def get(self,request,*args,**kwargs):
              data = Daybook_type.objects.all()
              serializer = Daybook_typeSerializer(data,many=True)
              return Response(serializer.data)
       
       def post(self,request,*args,**kwargs):
              serializer = Daybook_typeSerializer(data=request.data)
              if serializer.is_valid():
                     serializer.save()
                     return Response(serializer.data)
              return Response(serializer.errors)