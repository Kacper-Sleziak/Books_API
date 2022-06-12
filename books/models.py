from django.db import models


# Model of author


class Author(models.Model):
    full_name = models.CharField(
        max_length=50, null=False, blank=False, unique=True)

    def __str__(self):
        return self.full_name

# Model of Book


class Book(models.Model):
    external_id = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=50, null=False,
                             blank=False, unique=True)
    published_year = models.IntegerField(null=True, blank=True)
    acquired = models.BooleanField(default=False)
    thumbnail = models.URLField(max_length=256, null=True, blank=True)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title
