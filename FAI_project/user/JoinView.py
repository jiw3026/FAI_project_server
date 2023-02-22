import json
from .models import User
from django.views import View
from django.http import HttpResponse, JsonResponse

class JoinView(View):
    def post(self, request):
        data = json.loads(request.body)
        User.objects.create(
            user_email = data['user_email'],
            user_name = data['user_name'],
            user_password = data['user_password']
        )
        return HttpResponse(status=200)
    
    def get(self, request):
        user_data = User.objects.values()
        return JsonResponse({'users': list(user_data)}, status=200)
