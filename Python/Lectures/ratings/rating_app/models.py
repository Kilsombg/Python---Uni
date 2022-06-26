from django.db import models

# Create your models here.


class Information(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title
