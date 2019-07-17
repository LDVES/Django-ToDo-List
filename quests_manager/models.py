from django.db import models

# Create your models here.
class Quest(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=100)

    def __str__(self):
        return self.title
