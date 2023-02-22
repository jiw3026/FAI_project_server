import json
from .models import User
from django.views import View
from django.http import HttpResponse, JsonResponse

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if User.objects.filter(user_email = data['user_email']).exists():
                this_user = User.objects.get(user_email = data['user_email'])

                if this_user.user_password == data['user_password']:
                    return HttpResponse(status=200)
                return HttpResponse(status=401)
            return HttpResponse(status=400)
        
        except KeyError:
            return JsonResponse({'message':"INVALID_KEYS"}, status = 400)