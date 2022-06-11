from books.api.views import CreateBookView, BookDetailFilterView, BookIdView
from django.urls import path


urlpatterns = [
    path('create/', CreateBookView.as_view()),
    path('', BookDetailFilterView.as_view()),
    path("<int:pk>/", BookIdView.as_view()),
]
