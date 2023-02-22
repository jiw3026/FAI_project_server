from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Diagnosis
from user.models import User
from .serializer import DiagnosisSerializer
from .forms import *
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser


# Create your views here.

@csrf_exempt
def diagnosis(request):
    if request.method == 'POST':
        form = DiagnosisForm(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            return HttpResponse(status=201)
    else:
        form = DiagnosisForm()
    return HttpResponse(status=400)