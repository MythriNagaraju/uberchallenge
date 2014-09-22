from django.test import TestCase
from .models import FoodFacility
from .views import index
from django.contrib.auth.models import User

# Create your tests here.

class IndexView(TestCase):
    def test_valid_address_should_return_search_results(self):
	ff = FoodFacility.objects.all()[0]
	self.get_request = factory.get('/')
	#self.get_request.user = User.objects.create_user('testuser', password='secret')
	response = index(self.request)
	self.assertEqual(response.status_code, 200) 
