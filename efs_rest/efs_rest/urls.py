from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from portfolio import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('auth/', obtain_jwt_token),
    path('', views.todo_list),
    url(r'^api/todo/$', views.todo_list),
    url(r'^api/todo/(?P<pk>[0-9]+)$', views.getTodo),

]
