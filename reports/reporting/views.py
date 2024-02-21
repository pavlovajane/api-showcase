from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Report
from .serializers import ReportSerializer

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
    pass