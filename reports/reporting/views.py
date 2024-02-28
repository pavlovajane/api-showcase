from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Report
from rest_framework import status
from .serializers import ReportSerializer
from messaging.producer import *

# Create your views here.
@api_view(["GET"])
def list_reports(request):
    reports = Report.objects.all()
    serializer = ReportSerializer(reports, many = True)
    
    content = {
        "reports": serializer.data
    }

    return Response(content)

@api_view(["POST"])
def create_report(request):
    serializer = ReportSerializer(data=request.data)
    
    date = request.POST.get("date", None)
    if date is not None:
        if serializer.is_valid():
            try:
                message_id = send_message(serializer.data)
            except Exception as error:
                return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(message_id, status=status.HTTP_202_ACCEPTED)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
