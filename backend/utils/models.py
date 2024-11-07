from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        abstract = True


class Image(TimeStampedModel):
    file = models.ImageField(upload_to='images')
