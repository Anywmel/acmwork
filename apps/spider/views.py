import requests
from django.http import JsonResponse
from django.shortcuts import render
import json

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from spider import models
from users.models import UserProfile
from spider.tasks import task_vjudgebind


@csrf_exempt
def get_vjudge_info(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        print(json_data)
        username = request.POST.get('username', json_data.get('username'))
        name = request.POST.get('name', json_data.get('name'))
        url = "https://vjudge.net/user/solveDetail/"
        res = requests.post(url + username).json()
        data = {
            'code': 20000,
            'data': res
        }
        return JsonResponse(data)


def testvjudge(request):
    if request.method == 'GET':
        username = request.GET.get("vjudge")
        url = "https://vjudge.net/user/solveDetail/"
        res = requests.get(url + username)
        if res.status_code == 500:
            data = {
                'code': 500,
            }
        else:
            data = {
                'code': 20000,
            }
        return JsonResponse(data)


def vjudgebind(request):
    if request.method == 'GET':
        username = request.GET.get("vjudge")
        name = request.GET.get('username')
        userInfo = models.UserProfile.objects.get(username=name)
        userInfo.vjudge = username
        userInfo.save()
        url = "https://vjudge.net/user/solveDetail/"
        res = requests.get(url + username).json()
        task_vjudgebind.delay(username, name, res)
        data = {
            'code': 20000,
        }
        return JsonResponse(data)


def getList(request):
    if request.method == 'GET':
        username = request.GET.get("username")
        listInfo = models.ojDetail.objects.filter(oj_user=username)
        listInfoData = []
        for list in listInfo:
            id = list.id
            OJ = list.OJ
            Prob = list.Prob
            Accept = list.accept
            listData = {
                'id': id,
                'OJ': OJ,
                'Prob': Prob,
                'Accept': Accept,
                'username': username
            }
            listInfoData.append(listData)
        data = {
            'code': 20000,
            'data': listInfoData
        }
        return JsonResponse(data)


def getListTree(request):
    if request.method == 'GET':
        username = request.GET.get("username")
        url = "https://vjudge.net/user/solveDetail/"
        res = requests.get(url + username).json()
        acRecords = res['acRecords']
        acRe = []
        failRe = []
        for i in acRecords:
            temp = []
            for j in acRecords[i]:
                ProbData = {
                    'label': j
                }
                temp.append(ProbData)
            ojData = {
                'label': i,
                'children': temp
            }
            acRe.append(ojData)
        failRecords = res['failRecords']
        for i in failRecords:
            temp = []
            for j in failRecords[i]:
                ProbData = {
                    'label': j
                }
                temp.append(ProbData)
            ojData = {
                'label': i,
                'children': temp
            }
            failRe.append(ojData)
        resultData = {
            'label': 'acRecords',
            'children': acRe
        }
        # resultData = {
        #     {
        #         'label': 'acRecords',
        #         'children': acRe
        #     },
        #     {'label': 'failRecords',
        #      'children': failRe}
        # }
        print(resultData)
        return JsonResponse(resultData)


def insert_vjudge_info():
    print("insert")
    # acRecords = res["acRecords"]
    # failRecords = res["failRecords"]
    # # 写入acRecords

    print("ok!")
