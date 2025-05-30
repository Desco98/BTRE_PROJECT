from django.db import models
from django.utils import timezone

class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_time = models.DateTimeField(default=timezone.now, blank=True)
    user_id = models.IntegerField(blank=True)
    def __str__(self):
        return self.name