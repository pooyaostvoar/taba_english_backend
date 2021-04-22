import json
from django.test import Client
from django.test import TestCase


class AuthTestCase(TestCase):
	def setUp(self):
		pass

	def test_get_videos_list(self):
		test_cases = [
			{
				'url': '/videos/',
				'in': {},
				'out': {'status': 200}
			},
			{
				'url': '/videos/?page=1',
				'in': {'page': 1},
				'out': {'status': 200}
			},
		]
		c = Client()
		for test_case in test_cases:
			res = c.get(test_case['url'], test_case['in'])
			print(res)
