from django.urls import path
from . import views
from django.conf.urls import include
# from .views import JoinView, LoginView
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'user', views.UserViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('join/', include('rest_framework.urls')),
#     path('login/', include('rest_framework.urls'))
# ]

# urlpatterns = [
#     path('', JoinView.as_view()),
#     path('join/', JoinView.as_view()),
#     path('login/', LoginView.as_view())
# ]

urlpatterns = [
    path('join', views.user_join),
    path('get-user/<int:user_id>', views.user),
    path('login', views.user_login),
    path('auth', include('rest_framework.urls', namespace='rest_framework'))
] 