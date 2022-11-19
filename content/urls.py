from django.urls import path
from .views import UploadFeed


urlpatterns = [

    path('content/upload', UploadFeed.as_view())

]

