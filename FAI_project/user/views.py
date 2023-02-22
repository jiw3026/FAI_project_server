from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
# from rest_framework import viewsets
# from rest_framework import permissions
from .serializer import UserSerializer
from rest_framework.parsers import JSONParser

# Create your views here.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_class = [permissions.IsAuthenticated]

@csrf_exempt
def user_join(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def user(request, user_id):
    obj = User.objects.get(user_id = user_id)

    # 회원 정보 조회
    if request.method == 'GET':
        serializer = UserSerializer(obj)
        return JsonResponse(serializer.data, safe=False)
    # 회원 정보 수정
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    # 회원 탈퇴
    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)


    

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_email = data['user_email']
        obj = User.objects.get(user_email = search_email)

        if data['user_password'] == obj.user_password:
            serializer = UserSerializer(obj)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors, status=400)