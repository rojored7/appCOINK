import email
from statistics import mode
from django.db import models

class Usuario(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
        The variables to be used in the solved order are defined.
        Name: With a maximum space of 100 characters
        Email: With a maximum space of 100 characters
        city: With a maximum space of 100 characters
    """
    name_user = models.CharField(max_length=100)
    emai = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
