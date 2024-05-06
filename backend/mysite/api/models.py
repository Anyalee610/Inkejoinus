from django.db import models

# Create your models here.
class JoinUs(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    message = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return [self.firstname, self.email]