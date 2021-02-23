from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view


@api_view(['GET'])
def test(request):
    if request.method == 'GET':
        print(request.user)
        print(request.auth)
        return JsonResponse({"answer" : "200"}, status=200)

# Create your views here.
