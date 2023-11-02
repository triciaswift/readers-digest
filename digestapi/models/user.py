from django.db import models

class User(models.Model):
    """Database model for tracking users"""

    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    email = models.CharField(max_length=155)