from django.db import models

# Create your models here.



class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='books/')
    file = models.FileField(upload_to='books/')
    pages_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title