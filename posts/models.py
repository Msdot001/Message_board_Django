from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text}"