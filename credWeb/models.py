from django.db import models

# Create your models here.


class Record(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)

    def __str__(self) -> str:
        return (f"{self.firstName} {self.lastName}")
