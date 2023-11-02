from django.db import models

class Category(models.Model):
    """Database model for tracking categories"""

    name = models.CharField(max_length=155)