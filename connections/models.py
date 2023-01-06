from django.db import models


class Agreements(models.Model):
    username = models.CharField(max_length=128)
    email = models.CharField(max_length=128, unique=True)
    phone_number = models.CharField(max_length=128, unique=True)
    creation_date = models.DateField()
    conclusion_date = models.DateField()

    def __str__(self):
        return str(self.username)


class Connections(models.Model):
    city = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    house = models.CharField(max_length=128)
    connection_date = models.DateField()
    disconnection_date = models.DateField()
    agreement = models.OneToOneField(Agreements, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.city)
