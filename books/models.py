from django.db import models

# Model of Book


class Book(models.Model):
    external_id = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=50, null=False, blank=False, unique=True)
    published_year = models.IntegerField(null=True, blank=True)
    acquired = models.BooleanField(default=False)
    thumbnail = models.URLField(max_length=256, null=True, blank=True)

    # Function return list of authors'' full names 
    # (not author objects)
    def get_authors(self):
        list_of_authors = []
        queryset = AuthorBookRelation.objects.filter(book=self.id)

        for relation in queryset:
            list_of_authors.append(relation.author.full_name)

        return list_of_authors
    
    def __str__(self):
        return self.title


# AuthorBookRelation model was created to resolve problem of many to many
# relation beetwen book and author


class AuthorBookRelation(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.book.title} + {self.author.full_name}"

# Model of author


class Author(models.Model):
    full_name = models.CharField(
        max_length=50, null=False, blank=False, unique=True)
    
    def __str__(self):
        return self.full_name
    


    
    
