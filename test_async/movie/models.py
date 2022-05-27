from django.db import models

# Create your models here.


CATEGORY = (
    ("romance", "Romance"),
    ("action", "Action"),
    ("drama", "Drama"),
    ("games", "Games"),
    ("adventure", "Adventure"),
    ("comedy", "Comedy"),

)

class Movie(models.Model):
    title = models.CharField(max_length=250, default="")
    description = models.TextField(default="", blank=True)
    category = models.CharField(max_length=200, choices=CATEGORY)

    day = models.CharField(max_length=250, default="")
    date = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)
    uid = models.CharField(max_length=200)

    def __id__(self):
        return self.id


    def __str__(self):
        return self.title