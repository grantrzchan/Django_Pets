from django.conf.urls import url
from django.contrib import admin

from adoptions import views

#use raw string so that \ won't be use for escaping strings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    #Use (\d+) as regex to find ids as numbers, parantheses to include the \d+ as a group\
    #allows django to pass (\d+) as a parameter for views.py
    url(r'^adoptions/(\d+)/', views.pet_detail, name='pet_detail')
]
