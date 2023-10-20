import unittest

from utils import *
import requests
from cachetools import TTLCache
from datetime import date

class TestCircleArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(api_data(URL_API_ADDRESS[1],1),97.3074)
        self.assertEqual(api_data(URL_API_ADDRESS[2],2),96.73842)
        self.assertEqual(api_data(URL_API_ADDRESS[3],3),96.74)
        self.assertEqual(calc_rate(),f"Курс доллара на {date.today()}: {97.3074:.1f} руб.")
        self.assertEqual(calc_with_comission(7), [715.20939, 0.05, 97.3074])
#python -m unittest
