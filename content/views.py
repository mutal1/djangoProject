from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Feed
from uuid import uuid4
import os
from djangoProject.settings import MEDIA_ROOT
from user.models import User

# Create your views here.
class Main(APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id') # select * from content_feed

        email = request.session.get('email', None)

        if email is None:
            return render(request, "user/login.html")

        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request, "user/login.html")

        return render(request, "chansta/main.html", context=dict(feeds = feed_list, user=user))

class UploadFeed(APIView):
    def post(self, request):

        file = request.FILES['file']

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        file = request.data.get('file')
        image = uuid_name
        content = request.data.get('content')
        user_id = request.data.get('user_id')
        profile_image = request.data.get('profile_image')

        Feed.objects.create(image=image, content=content, user_id=user_id, profile_image=profile_image, like_count=0)


        print(file)
        print(image)

        return Response(status=200)


