from django.db import models

# Create your models here.


class TraceEvent(models.Model):

    eventstring = models.TextField(null=True)
    # Fields for timestamp and logging purposes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
