"""
Sample tests
"""
from django.test import SimpleTestCase

from app import  cal


class TestCalc(SimpleTestCase):
    def test_add(self):
        res = cal.add(5, 6)

        self.assertEqual(res, 11)   # assertEqual is a method of SimpleTestCase

    def test_subtract(self):
        res = cal.subtract(5, 6)

        self.assertEqual(res, -1)
