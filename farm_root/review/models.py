from django.db import models

class Review(models.Model):
    customer = models.CharField(max_length=50)
    review = models.TextField()
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.customer
