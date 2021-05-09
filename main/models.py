from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Info(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=100, null=True)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    dep = models.CharField(max_length=200)
    roll = models.CharField(max_length=100, null=True)
    github = models.CharField(max_length=100, null=True)
    linkedin = models.CharField(max_length=100, null=True)
    portfolio = models.CharField(max_length=100, null=True)

    clg = models.CharField(max_length=100, null=True)
    clg_cg = models.CharField(max_length=100, null=True)
    start_clg = models.CharField(max_length=100, null=True)
    end_clg = models.CharField(max_length=100, null=True)

    edu = models.CharField(max_length=100, null=True)
    edu_cg = models.CharField(max_length=100, null=True)
    start_edu = models.CharField(max_length=100, null=True)
    end_edu = models.CharField(max_length=100, null=True)

    exp1 = models.CharField(max_length=100, null=True)
    start_exp1 = models.CharField(max_length=100, null=True)
    end_exp1 = models.CharField(max_length=100, null=True)
    exp1_info = models.TextField(max_length=10000, null=True)

    exp2 = models.CharField(max_length=100, null=True)
    start_exp2 = models.CharField(max_length=100, null=True)
    end_exp2 = models.CharField(max_length=100, null=True)
    exp2_info = models.TextField(max_length=10000, null=True)

    exp3 = models.CharField(max_length=100, null=True)
    start_exp3 = models.CharField(max_length=100, null=True)
    end_exp3 = models.CharField(max_length=100, null=True)
    exp3_info = models.TextField(max_length=10000, null=True)

    pj1 = models.CharField(max_length=100, null=True)
    start_pg1 = models.CharField(max_length=100, null=True)
    end_pg1 = models.CharField(max_length=100, null=True)
    pg1_info = models.TextField(max_length=10000, null=True)

    pj2 = models.CharField(max_length=100, null=True)
    start_pg2 = models.CharField(max_length=100, null=True)
    end_pg2 = models.CharField(max_length=100, null=True)
    pg2_info = models.TextField(max_length=10000, null=True)

    pj3 = models.CharField(max_length=100, null=True)
    start_pg3 = models.CharField(max_length=100, null=True)
    end_pg3 = models.CharField(max_length=100, null=True)
    pg3_info = models.TextField(max_length=10000, null=True)

    Achievments = models.TextField(max_length=10000, null=True)
    Skills = models.TextField(max_length=10000, null=True)
    Por = models.TextField(max_length=10000, null=True)
    Hobbies = models.TextField(max_length=10000, null=True)

    def __str__(self):
        return self.profile_name
