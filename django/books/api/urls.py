from django.urls import path
from books.api.views import CreateBookView

urlpatterns = [
    path('create/', CreateBookView.as_view()),
]
