from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import ItemSerializer
from .models import items

@api_view(['GET'])
def itemList(request):
    item = items.objects.all()
    serializer = ItemSerializer(item, many=True)
    return Response(serializer.data)

