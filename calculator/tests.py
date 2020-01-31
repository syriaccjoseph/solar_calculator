# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client

class CalculatorTest(TestCase):
    def setUp(self):
        client = Client()
    
    def test_redirect(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/calculator/')

    def test_calculator_status(self):
        response = self.client.get('/calculator/')
        self.assertEqual(response.status_code, 200)

    def test_calculator_context(self):
        response = self.client.post('/calculator/', {'area': 12})
        self.assertEqual(response.context['area'], '12.0')
        self.assertEqual(response.context['nominal_power'], '183735.0')


