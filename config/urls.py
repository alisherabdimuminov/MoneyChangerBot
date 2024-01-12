from django.contrib import admin
from django.urls import path, include

from transactions.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("transactions.urls")),
    path('', home, name="home")
]
