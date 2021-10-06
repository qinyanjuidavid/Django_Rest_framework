from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/postings/', include('posting.api.urls',
                                  namespace="api-postings"),),

    path('api-token-auth/', obtain_jwt_token, name="api-login")
]
