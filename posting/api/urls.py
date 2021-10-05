from django.urls import path
from posting.api import views
from posting.api.views import BlogPostRudView
app_name = "posting"

urlpatterns = [
    path('<pk>/', BlogPostRudView.as_view(), name="post-rud")
]
