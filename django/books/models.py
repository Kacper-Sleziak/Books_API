from django.db import models

# Models of Book


class Book(models.Model):
    external_id = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=50, null=False, blank=False)
    published_year = models.IntegerField(null=False, blank=False)
    acquired = models.BooleanField(default=False)
    thumbnail = models.URLField(max_length=256, null=True, blank=True)

    def get_authors(self):
        list_of_authors = []
        queryset = AuthorBookRelation.objects.filter(book=self.id)

        for relation in queryset:
            list_of_authors.append(relation.author.full_name)

        return list_of_authors

# AuthorBookRelation model was created to resolve problem of many to many
# relation beetwen book and author


class AuthorBookRelation(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

# Model of author


class Author(models.Model):
    full_name = models.CharField(
        max_length=50, null=False, blank=False, unique=True)
    


    
    
