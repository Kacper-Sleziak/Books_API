from django.contrib import admin
from django.urls import path, include 
from core.api.views import api_spec_view, BookImportView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_spec/', api_spec_view),
    path('import/', BookImportView.as_view()),
    path('books/', include('books.api.urls'))
]
