from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/postings/', include('posting.api.urls',
                                  namespace="api-postings"),)
]
