from django.contrib import admin
from django.urls import path, include
from core.api.views import api_spec_view, BookImportView
from core.views import index_view

urlpatterns = [
    path('', index_view),
    path('admin/', admin.site.urls),
    path('api_spec/', api_spec_view),
    path('import/', BookImportView.as_view()),
    path('books/', include('books.api.urls'))
]
