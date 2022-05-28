from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api_spec/', ),
    path('books/', include('books.api.urls')),
]
