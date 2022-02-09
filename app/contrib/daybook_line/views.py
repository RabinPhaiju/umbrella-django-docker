from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Daybook_lineSerializer
from .models import Daybook_line


class Daybook_lineView(APIView):
       def get(self,request,*args,**kwargs):
              data = Daybook_line.objects.all()
              serializer = Daybook_lineSerializer(data,many=True)
              return Response(serializer.data)
       
       def post(self,request,*args,**kwargs):
              serializer = Daybook_lineSerializer(data=request.data)
              if serializer.is_valid():
                     serializer.save()
                     return Response(serializer.data)
              return Response(serializer.errors)