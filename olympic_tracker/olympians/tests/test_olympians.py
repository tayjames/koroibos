from django.test import TestCase
from django.test import Client
from ..models import Olympian
import json

class GetOlympiansTest(TestCase):

    def setUp(self):
        self.client = Client()
        Olympian.objects.create(
            name="Tay Jimenez", sex="M", age="26", height="180", weight="61", team="Mexico", games="Summer 2016", sport="Tennis", event="Mens Singles", medal="Silver"
        )
        Olympian.objects.create(
            name="Teena Marie", sex="F", age="39", height="180", weight="61", team="Poland", games="Summer 2016", sport="Weightlifting", event="Women's Benchpress", medal="Gold"
        )
        Olympian.objects.create(
            name="Paula Abdul", sex="F", age="47", height="180", weight="61", team="Phillipines", games="Summer 2016", sport="Swimming", event="Freestly", medal="Bronze"
        )

    def test_get_all_olympians(self):
        response = self.client.get('http://localhost:8000/api/v1/olympians')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0].__contains__('name'), True)
        self.assertEqual(response.data[0].__contains__('team'), True)
        self.assertEqual(response.data[0].__contains__('age'), True)
        self.assertEqual(response.data[0].__contains__('sport'), True)
        self.assertEqual(response.data[0].__contains__('medal'), True)
        self.assertEqual(len(response.data), 3)

    def test_get_youngest_olympian(self):
        response = self.client.get('http://localhost:8000/api/v1/olympians?age=youngest')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], 'Tay Jimenez')
        self.assertEqual(len(response.data), 1)

    def test_get_oldest_olympian(self):
        response = self.client.get('http://localhost:8000/api/v1/olympians?age=oldest')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], 'Paula Abdul')
        self.assertEqual(len(response.data), 1)
