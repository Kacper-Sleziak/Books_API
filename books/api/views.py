from books.api.serializers import BookSerializer
from rest_framework import status, views
from books.models import Book
from rest_framework.response import Response

# This function help to add additional to book's serializer
# response


def add_authors_to_response_data(response_data, book):
    authors = book.get_authors()

    # Adding list of authors'' names to reponse
    response_data['authors'] = authors
    return response_data


class BookDetailFilterView(views.APIView):
    serializer_class = BookSerializer

    def get(self, request, format=None):
        queryset = self.get_queryset(request)
        serializer = self.serializer_class(queryset, many=True)

        if queryset.exists():
            response_data = serializer.data
            for i in range(len(queryset)):
                book = queryset[i]
                response_data[i] = add_authors_to_response_data(
                    response_data[i], book)

            return Response(response_data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self, request):
        query_p = request.query_params
        queryset = Book.objects.all()

        if 'title' in query_p:
            title = query_p['title']
            queryset = queryset.filter(title=title)

        if 'from' in query_p:
            from_year = int(query_p['from'])
            queryset = queryset.filter(published_year__gte=from_year)

        if 'to' in query_p:
            from_year = int(query_p['to'])
            queryset = queryset.filter(published_year__lte=from_year)

        if 'acquired' in query_p:
            acquired = query_p['acquired']

            if acquired == 'false':
                acquired = False
            elif acquired == 'true':
                acquired = True

            queryset = queryset.filter(acquired=acquired)

        # This statment check if any of books in queryset
        # has full_name that contain autor parm
        # for example if author = J. R. R. Tolkien"
        # and parm = tolkien, statment will return this book
        # in queryset

        if 'author' in query_p:
            author = query_p['author']
            found_books_ids = []

            # Checking every book in actual queryset
            for book in queryset:
                book_authors = book.get_authors()
                # Checking every author of book
                for book_author in book_authors:
                    # Add if full_name contains author param
                    if author.lower() in str(book_author).lower():
                        found_books_ids.append(book.id)
                        break

            queryset = Book.objects.filter(id__in=found_books_ids)

        return queryset


# [POST, GET] view for creating book


class CreateBookView(views.APIView):
    serializer_class = BookSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            if 'authors' in request.data:
                authors = request.data['authors']
                new_book = serializer.create(serializer.data, authors=authors)
            else:
                new_book = serializer.create(serializer.data)

            book_serializer = BookSerializer(new_book)

            response_data = add_authors_to_response_data(
                book_serializer.data, new_book)

            return Response(
                response_data,
                status.HTTP_201_CREATED)
        return Response(
            status=status.HTTP_400_BAD_REQUEST)

# [GET, POST, DELETE] View for basic operations
# on single book


class BookIdView(views.APIView):
    serializer_class = BookSerializer

    def is_book_with_given_id(self, pk):
        queryset = Book.objects.filter(id=pk)

        if queryset.exists():
            return True
        else:
            return False

    def get(self, request, pk, format=None):
        if self.is_book_with_given_id(pk):
            book = Book.objects.get(id=pk)
            serializer = self.serializer_class(book)

            response_data = add_authors_to_response_data(
                serializer.data, book)
            
            return Response(
                response_data, status=status.HTTP_200_OK)

        return Response(
            status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        if self.is_book_with_given_id(pk):
            book = Book.objects.get(id=pk)
            serializer = self.serializer_class(book, request.data)
            if serializer.is_valid():
                book = serializer.save()

                response_data = add_authors_to_response_data(
                    serializer.data, book)

                return Response(response_data,
                                status=status.HTTP_200_OK)

            return Response(
                status=status.HTTP_400_BAD_REQUEST)

        return Response(
            status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk, fromat=None):
        if self.is_book_with_given_id(pk):
            book = Book.objects.get(id=pk)
            book.delete()
            return Response(
                status=status.HTTP_200_OK)

        return Response(
            status=status.HTTP_204_NO_CONTENT)
