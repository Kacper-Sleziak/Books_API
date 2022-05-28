from books.api.serializers import BookSerializer
from rest_framework import status
from rest_framework import views
from books.models import Book
from rest_framework.response import Response


# [POST] End point for creating
class CreateBookView(views.APIView):
    serializer_class = BookSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            authors = request.data['authors']
            new_book = serializer.create(serializer.data, authors=authors)
            authors = new_book.get_authors()

            book_serializer = BookSerializer(new_book)
            response_data = book_serializer.data

            # Adding list of authors'' names to reponse
            response_data['authors'] = authors

            return Response(
                response_data,
                status.HTTP_201_CREATED)
        return Response(
            status=status.HTTP_400_BAD_REQUEST)
