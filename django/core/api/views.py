from rest_framework.decorators import api_view
from rest_framework import status, views
from books.api.serializers import BookSerializer
from rest_framework.response import Response
from books.models import Book, Author, AuthorBookRelation
import requests


@api_view(['GET'])
def api_spec_view(request):
    if request.method == 'GET':
        response = {"info": {
            "version": "2022.05.16"
        }}

        return Response(
            response, status=status.HTTP_200_OK)


class BookImportView(views.APIView):
    def post(self, request, format=None):
        author_param = request.data['author']

        google_response = requests.get(
            f'https://www.googleapis.com/books/v1/volumes?q={author_param}')

        items = google_response.json()['items']
        imported_books = 0

        # Unpacking json response
        for item in items:

            volume_info = item['volumeInfo']
            is_author_matching_parm = False

            if 'authors' in volume_info:
                for author in volume_info['authors']:
                    if author_param.lower() in author.lower():
                        is_author_matching_parm = True

            if is_author_matching_parm:
                external_id = None
                if 'id' in item:
                    external_id = item['id']

                title, authors, published_year, thubnail = self.unpack_volume(
                    volume_info)

                # Update book if exsists in data base.
                # As an exsisting book i mean the one with
                # same title as item fetched from google
                queryset = Book.objects.filter(title=title)

                if queryset.exists():
                    book = queryset[0]

                    self.update_exsisting_book(book, authors,
                                               external_id, published_year, thubnail)
                else:
                    self.create_new_book(external_id, title, authors,
                                         published_year, thubnail)
                    imported_books += 1

        imported_info = {'imported': imported_books}
        return Response(
            imported_info, status=status.HTTP_200_OK
        )

    def unpack_volume(self, volume_info):
        title = None
        if 'title' in volume_info:
            title = volume_info['title']

        authors = None
        if 'authors' in volume_info:
            authors = volume_info['authors']

        published_year = None
        if 'publishedDate' in volume_info:
            published_year = volume_info['publishedDate']
            published_year_arr = published_year.split('-')
            published_year = published_year_arr[0]

        thumbnail = None
        if 'imageLinks' in volume_info:
            images = volume_info['imageLinks']
            if 'thumbnail' in images:
                thumbnail = images['thumbnail']

        return (title, authors,
                published_year, thumbnail)

    def create_new_book(self, external_id, title,
                        authors, published_year, thumbnail):

        book = Book.objects.create(external_id=external_id, title=title,
                                   published_year=published_year, thumbnail=thumbnail)

        if authors != None:
            for author in authors:
                queryset = Author.objects.filter(full_name=author)

                if not queryset.exists():
                    author = Author.objects.create(full_name=author)
                    AuthorBookRelation.objects.create(book=book, author=author)
                else:
                    author = queryset[0]
                    AuthorBookRelation.objects.create(book=book, author=author)
                    

    def update_exsisting_book(self, book, authors,
                              external_id, published_year, thumbnail):

        if external_id != None:
            book.external_id = external_id

        if published_year != None:
            book.published_year = published_year

        if thumbnail != None:
            book.thumbnail != None

        book.save()
        book_authors = book.get_authors()

        # Updating authors and book relations
        # for author fetched from google

        def update_books_authors(author_name, book):
            author_queryset = Author.objects.filter(full_name=author_name)

            author = None
            if author_queryset.exists():
                author = author_queryset[0]
            else:
                author = Author.objects.create(full_name=author_name)

            AuthorBookRelation.objects.create(
                book=book, author=author)

        if authors != None:
            for author in authors:
                # book_authors are authors from actual db
                if not author in book_authors:
                    update_books_authors(author, book)
