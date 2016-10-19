from django.conf.urls import patterns,url,include

urlpatterns = [
    url(r'^', include('main.urls')),
]
