from __future__ import absolute_import

import requests
from celery import shared_task
from spider import models


@shared_task
def task_vjudgebind(username, name, res):
    userDelete = models.ojDetail.objects.filter(user=name).delete()
    acRecords = res['acRecords']
    failRecords = res['failRecords']
    print(failRecords)
    for i in acRecords:
        for j in acRecords[i]:
            models.ojDetail(OJ=i, Prob=j, accept="True", oj_user=username, user=name).save()

    for i in failRecords:
        for j in failRecords[i]:
            models.ojDetail(OJ=i, Prob=j, accept="False", oj_user=username, user=name).save()
