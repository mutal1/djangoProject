
from django.shortcuts import render
from rest_framework.views import APIView


class Sub(APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        print("겟으로 호출")
        return render(request, "chansta/main.html")

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        print("포스트로 호출")
        return render(request, "chansta/main.html")
