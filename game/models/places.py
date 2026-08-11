from django.db import models


class Region(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="regions/", null=True, blank=True)

    def __str__(self):
        return self.title
