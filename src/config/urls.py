
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("apps.user.urls")),
    path('', include("apps.book.urls")),
]
