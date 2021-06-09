from login_app import views
from django import urls
from django.urls.conf import include
from django.urls import path, include


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index)
]