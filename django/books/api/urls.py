from django.urls import path
from books.api.views import CreateBookView, BookIdView, BookDetailFilterView

urlpatterns = [
    path('create/', CreateBookView.as_view()),
    path("<int:pk>/", BookIdView.as_view()),
    path('', BookDetailFilterView.as_view()),
]
