from django.db import models
from digestapi.models import Book
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    comment = models.CharField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)