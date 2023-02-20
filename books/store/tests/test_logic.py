from django.test import TestCase
# from unittest import TestCase
from .logic import operations


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(1, 1, '+')
        self.assertEqual(result, 2)

    def test_minus(self):
        result = operations(6, 2, '-')
        self.assertEqual(result, 4)

    def test_myltiply(self):
        result = operations(6, 2, '*')
        self.assertEqual(result, 12)

