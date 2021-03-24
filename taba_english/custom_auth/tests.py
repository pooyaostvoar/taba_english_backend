
import json
from django.test import Client
from django.test import TestCase

class AuthTestCase(TestCase):
	def setUp(self):
		pass

	def test_register(self):
		test_cases = [
			{'in': {'password': '123', 'email': 'pooya@gmail.com', 'username': 'pooya@gmail.com'},
			 'out': {'status': 201}},
			{'in': {'password': '123', 'email': 'pooya@gmail.com', 'username': 'pooya@gmail.com'},
			 'out': {'status': 400}},
		]
		c = Client()
		for test_case in test_cases:
			res = c.post('/auth/register/', test_case['in'])
			self.assertEqual(res.status_code, test_case['out']['status'])

	def test_login(self):
		test_cases = [
			{
				'url': '/auth/register/',
			 	'in': {'password': '123', 'email': 'pooya1@gmail.com', 'username': 'pooya@gmail.com'},
			 	'out': {'status': 201}
			},
			{
				'url': '/auth/login/',
				'in': {'password': '123', 'email': 'pooya1@gmail.com', 'username': 'pooya@gmail.com'},
				'out': {'status': 200}
			},
			{
				'url': '/auth/login/',
				'in': {'password': '12', 'email': 'pooya1@gmail.com', 'username': 'pooya@gmail.com'},
				'out': {'status': 401}
			}
		]
		c = Client()
		for test_case in test_cases:
			res = c.post(test_case['url'], test_case['in'])
			self.assertEqual(res.status_code, test_case['out']['status'])
