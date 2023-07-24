
from django.contrib import admin
from django.urls import path
from smsapp.views import home,create,remove

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('create/',create,name="create"),
    path('remove/<int:id>',remove,name="remove")
]
