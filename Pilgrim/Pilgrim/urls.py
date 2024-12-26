


from django.contrib import admin
from django.urls import path, re_path
from app.views import *
from django.contrib.auth.views import LoginView, LogoutView
# from app.views import viewer

from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('write/', write_zapis, name='write_zapis'),
    path('delete/<int:zapis_id>/', delete_zapis, name='delete_zapis'),
    path('', all_zapis, name='all_zapis'),
    
]
