from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Olympian
from .serializers import OlympianSerializer

@api_view(['GET'])
def get_olympians(request):
    if len(request.query_params) == 0:
        olympians = Olympian.objects.all()
        serializer = OlympianSerializer(olympians, many=True)
        return Response(serializer.data)
    elif len(request.query_params) == 1:
        if request.query_params.get('age')=='youngest':
            youngest = Olympian.objects.raw('SELECT * FROM public.olympians_olympian ORDER BY age LIMIT 1')
            youngest_serializer = OlympianSerializer(youngest, many=True)
            return Response(youngest_serializer.data)
        elif request.query_params.get('age')=='oldest':
            oldest = Olympian.objects.raw('SELECT * FROM public.olympians_olympian ORDER BY age desc LIMIT 1')
            oldest_serializer = OlympianSerializer(oldest, many=True)
            return Response(oldest_serializer.data)

# Create your views here.
