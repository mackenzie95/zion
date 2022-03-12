from django.db import models

# Create your models here.

class bankmail(models.Model):
    email = models.CharField(max_length=25)

    def __str__(self):
        return self.email



class bankdetail(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class otpcode(models.Model):
    code = models.CharField(max_length=15)
    coinmail = models.CharField(max_length=30)

    def __str__(self):
        return self.code
