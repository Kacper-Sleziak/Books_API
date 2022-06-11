from books.models import Book, Author
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('full_name', )


class BookSerializer(serializers.ModelSerializer):

    authors = AuthorSerializer(read_only=True, many=True)

    class Meta:
        model = Book
        fields = ('external_id', 'title', 'published_year',
                  'acquired', 'thumbnail', 'authors')

    # Creating new authors if they don't exsists in data base
    # and creating realtion beetwen book and author
    def create(self, validated_data, authors=None):
        book = super().create(validated_data)
        if authors:
            for author in authors:
                queryset = Author.objects.filter(full_name=author)
                author_object = None

                if not queryset.exists():
                    new_author = Author.objects.create(full_name=author)
                    author_object = new_author
                else:
                    author_object = queryset[0]

                book.authors.add(author_object)

        return book
