from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from report.models import reportLog
from report.serializers import reportLogSerializer


@api_view(['GET'])
def getLogs(request):
    if request.method == 'GET':
        print(request.user)
        print(request.auth)
        logs = reportLog.objects.filter(reportUser=request.user)
        serializer = reportLogSerializer(logs, many=True)
        return JsonResponse({"data": serializer.data}, status=200, safe=True)
@api_view(['GET'])
def test(request):
    if request.method == 'GET':
        print(request.user)
        print(request.auth)

        return JsonResponse({"answer" : "200"}, status=200)

@api_view(['POST'])
def report(request):
    if request.method == 'POST':
        print(request.user)
        print(request.auth)
        rl = reportLog(reportData=request.data.get('data'), reportUser=request.user)
        rl.save()
        return JsonResponse({"answer" : "200"}, status=200)

# Create your views here.
