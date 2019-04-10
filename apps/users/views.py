from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework_jwt.utils import jwt_decode_handler
from django.contrib.auth import get_user_model

from users import models
from users.serializers import UserDetailSerializer
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
import json

# Create your views here.
User = get_user_model()


def get_user_info(request):
    # 通过token查询用户信息
    if request.method == 'GET':
        token = request.GET.get('token')
        token_user = []
        token_user = jwt_decode_handler(token)
        user_id = token_user["user_id"]
        user_info = User.objects.get(pk=user_id)
        serializer = UserDetailSerializer(user_info)
        data = {
            "data": serializer.data,
            "code": 20000,
            "messgae": "succeed"
        }
        return JsonResponse(data)


@csrf_exempt
def logout(request):
    if request.method == 'POST':
        data = {
            "code": 20000,
            "status": 'success'
        }
        return JsonResponse(data)


@csrf_exempt
def register(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        username = request.POST.get('username', json_data.get('username'))
        password = request.POST.get('password', json_data.get('password'))
        email = request.POST.get('email', json_data.get('email'))
        data = {
            "code": 20000,
            "status": 'success'
        }
        User.objects.create_user(username, email, password)
        return JsonResponse(data)


@csrf_exempt
def save_user_info(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        username = request.POST.get('username', json_data.get('username'))
        password = request.POST.get('password', json_data.get('password'))
        email = request.POST.get('email', json_data.get('email'))
        status = ''
        userInfo = models.UserProfile.objects.get(username=username)
        if password is '' and email is '':
            status = '未修改'
        elif password is '' and email is not '':
            userInfo.email = email
            userInfo.save()
            status = 'email更新成功'
        elif password is not '' and email is '':
            userInfo.set_password(password)
            userInfo.save()
            status = '密码更新成功'
        else:
            userInfo.email = email
            userInfo.set_password(password)
            userInfo.save()
            status = 'email和密码更新成功'
        data = {
            "code": 20000,
            "status": status
        }
        return JsonResponse(data)
