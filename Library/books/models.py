from pyexpat import model
from turtle import title
from django.db import models
from django.contrib.auth import get_user_model
from django import forms

Rate = (
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
    ("5", "Five"),
)

class Book(models.Model):
    title = models.CharField(max_length= 125)
    subtitle = models.CharField(max_length= 100)
    author = models.TextField()
    review_date = models.DateField()
    isbn =  models.CharField(max_length= 13 )
    # ISBN is a unique, 13-character identifier assigned to every published book.
    reviewer = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    price =models.IntegerField( default= None)
#     Rate = (
#     ("1", "One"),
#     ("2", "Two"),
#     ("3", "Three"),
#     ("4", "Four"),
#     ("5", "Five"),
# )
    # review_date = models.DateTimeField(auto_now_add= True , auto_now= True , auto_created= True)

    def __str__(self):
        return self.title 