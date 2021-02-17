from django.test import TestCase
import json
from django.test import Client
# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
class AuthTestCase(TestCase):
	def setUp(self):
		pass
	def test_register(self):
		test_cases = [
				{'in': {'username': 'pooya', 'password': '123', 'email': 'pooya@gmail.com'}, 'out':{'status':200}},
				{'in': {'username': 'pooya1', 'password': '123', }, 'out': {'status': 200}},
				{'in': {'username': 'pooya', 'password': '123', 'email': 'pooya@gmail.com'}, 'out': {'status': 200}},
		]
		c= Client()
		for test_case in test_cases:
			res = c.post('/auth/register/', test_case['in'])
			print(res)
			#self.assertEqual(json.loads(res.status_code), test_case['out'])