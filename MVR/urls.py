from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showmain, name="showmain"),
    path('accounts/',include('allauth.urls')),
    path('mypage/',include('mypage.urls')),
    path('review',views.showmovie, name="showmovie")
]
