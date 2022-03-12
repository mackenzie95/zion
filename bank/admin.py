from django.contrib import admin

from .models import bankmail, bankdetail, otpcode

# Register your models here.

admin.site.register(bankmail)
admin.site.register(bankdetail)
admin.site.register(otpcode)
