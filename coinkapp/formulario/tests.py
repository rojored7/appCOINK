import datetime
from urllib import response

from django.test import TestCase
from django.urls.base import reverse

from urllib import response
from .models import User

# Create your tests here.
def test_etUpTestData(cls):
    print("setUpTestData: Run once to set up non-modified data for all class methods.")
    pass
#Pruena de creacion de usuario 
class Creacion_usuario(TestCase):
    
    def test_User_creatio(self):
        
        user = User.objects.create(
            name_user="RED",
            emai="RED@RED.com",
            ciudad="REDPOLIS" 
        )
        self.assertTrue(user.name_user == "RED")
