from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Olympian
from .serializers import OlympianSerializer
from django.db import connection

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

@api_view(['GET'])
def olympian_stats(request):
    # breakpoint()
    olympians = Olympian.objects.all()
    male_weight = "SELECT AVG(CAST(weight as int)) FROM public.olympians_olympian WHERE weight ~ '^[0-9]+$' and sex='M';"
    female_weight = "SELECT AVG(CAST(weight as int)) FROM public.olympians_olympian WHERE weight ~ '^[0-9]+$' and sex='F';"
    total_competing_olympians = "SELECT COUNT(DISTINCT name) FROM public.olympians_olympian"
    average_age = "SELECT AVG(CAST(age as int)) FROM public.olympians_olympian WHERE age ~ '^[0-9]+$';"

    cursor = connection.cursor()

    result1 = cursor.execute(male_weight)
    fetch1 = cursor.fetchone()[0]

    result2 = cursor.execute(female_weight)
    fetch2 = cursor.fetchone()[0]

    result3 = cursor.execute(total_competing_olympians)
    fetch3 = cursor.fetchone()[0]

    result4 = cursor.execute(average_age)
    fetch4 = cursor.fetchone()[0]

    average_weights = {"unit": "kg",
        "male_olympians": round(fetch1),
        "female_olympians": round(fetch2)
    }

    stats = {
        "olympian_stats": {
        "total_competing_olympians": fetch3,
        "average_weight": average_weights,
        "average_age": round(fetch4)
    }
}

    return Response([stats])

# Create your views here.
