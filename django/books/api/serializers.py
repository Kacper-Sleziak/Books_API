from rest_framework import serializers
from books.models import Book, Author, AuthorBookRelation


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.ListField(write_only=True, required=False)

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
                AuthorBookRelation.objects.create(
                    author=author_object, book=book)
        return book
    

        
