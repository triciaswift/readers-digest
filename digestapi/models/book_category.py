from django.db import models

class BookCategory(models.Model):
    """Database model for tracking book categories"""

    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="book_categories")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="book_categories")
    timestamp = models.DateTimeField(auto_now_add=True)