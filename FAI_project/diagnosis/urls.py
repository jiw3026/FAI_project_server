from django.urls import path
from . import views
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('upload-diagnosis/<int:user_id>', views.diagnosis),
    path('upload-diagnosis', views.diagnosis),
    path('auth', include('rest_framework.urls', namespace='rest_framework'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)