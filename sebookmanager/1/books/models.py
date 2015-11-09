from django.db import models

class Author(models.Model):
    AuthorId = models.IntegerField()
    Name = models.CharField(max_length=40)
    Age = models.IntegerField()
    Country = models.CharField(max_length=40)
    def __unicode__(self):
        return self.AuthorId

class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    Title = models.CharField(max_length=100)
    AuthorId = models.ForeignKey(Author)
    Publisher = models.CharField(max_length=100)
    PublishDate = models.DateField()
    Price = models.IntegerField()
    def __unicode__(self):
        return self.Title
class test(models.Model)
    test=models.CharField(max_length=10)