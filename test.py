from unittest import TestCase
from app import app
from conversion import Conversion


class Tests(TestCase):

    def test_home(self):
        with app.test_client() as client:

            response = client.get("/")
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn("<h1>Forex Converter</h1>", html)

    def test_clean_convert(self):
        with app.test_client() as client:

            response = client.get("/convert?from=USD&to=USD&amount=13")
            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn("<p>The rate is 1.0</p>", html)
            self.assertIn("<p>The converted amount is US$13.0</p>", html)

    def test_invalid_from(self):
        with app.test_client() as client:

            response = client.get("/convert?from=ZZZ&to=USD&amount=100")

            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, "http://localhost/")

    def test_invalid_to(self):
        with app.test_client() as client:

            response = client.get("/convert?from=USD&to=YYY&amount=100")

            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, "http://localhost/")

    def test_invalid_amount(self):
        with app.test_client() as client:

            response = client.get("/convert?from=USD&to=EUR&amount=text")

            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, "http://localhost/")

    def test_invalid_all(self):
        with app.test_client() as client:

            response = client.get("/convert?from=XXX&to=ZZZ&amount=text")

            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, "http://localhost/")
