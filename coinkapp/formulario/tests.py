from django.test import TestCase
from django.urls.base import reverse

from urllib import response
from .models import User
# Create your tests here.


class MultipleUser(TestCase):
    
    
    def test_was_published_same_register(self):
        
        
        repetido = User(name_user="COINK",emai="COINK", ciudad="COINK")
        self.assertIs(repetido(),False)
 
class FormularioIndexViewTests(TestCase):

    def test_no_user(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        #self.assertContains(response,text= "No polls are avaible.")
        self.assertQuerysetEqual(response.context["lastest_question_list"],[])
               