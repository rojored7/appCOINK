from django.test import TestCase
from django.urls.base import reverse

from urllib import response
from .models import User
# Create your tests here.

#Pruena de creacion de usuario 
def User_creatio():
    user=User.objects.create_user(
        name_user="RED",
        emai="RED@RED.com",
        ciudad="REDPOLIS"    
    )
    assert user.name_user == "RED"
 
