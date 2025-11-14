from django.db import models

# Create your models here.

class Bookstore(models.Model):
    Author_name=models.CharField(max_length=200)
    Book_summary=models.CharField(max_length=200)
    Book_journal=models.CharField(max_length=200)
    Book_name=models.CharField(max_length=200)

    def __str__(self):
        return self.Book_name


