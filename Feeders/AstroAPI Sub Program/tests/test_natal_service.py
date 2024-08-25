import unittest
from astroapi.services.natal_service import generate_natal_chart

class TestNatalService(unittest.TestCase):
    def test_generate_natal_chart(self):
        birth_data = {"date": "1990-01-01", "time": "12:00", "location": "New York, NY"}
        chart = generate_natal_chart(birth_data)
        self.assertIsNotNone(chart)