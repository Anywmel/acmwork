from django.db import models

# Create your models here.
from users.models import UserProfile


class ojDetail(models.Model):
    OJ = models.CharField(max_length=20, verbose_name="OJ平台")
    Prob = models.CharField(max_length=20, verbose_name="题目ID")
    accept = models.CharField(max_length=5, verbose_name="通过情况")
    oj_user = models.CharField(max_length=100, verbose_name="oj用户名")
    user = models.CharField(max_length=100, verbose_name="用户名")

    class Meta:
        verbose_name = "OJ记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.OJ
