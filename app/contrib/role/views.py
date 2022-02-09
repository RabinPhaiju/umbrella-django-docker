from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RoleSerializer
from .models import Role


class RoleView(APIView):
       def get(self,request,*args,**kwargs):
              data = Role.objects.all()
              serializer = RoleSerializer(data,many=True)
              return Response(serializer.data)
       
       def post(self,request,*args,**kwargs):
              serializer = RoleSerializer(data=request.data)
              if serializer.is_valid():
                     serializer.save()
                     return Response(serializer.data)
              return Response(serializer.errors)