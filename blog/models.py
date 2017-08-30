from django.db import models

# Create your models here.

class Stories(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    summary = models.TextField()
    tag = models.CharField(max_length = 200)
    image_url = models.URLField()
    url = models.URLField()
    source = models.CharField(max_length = 200)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title