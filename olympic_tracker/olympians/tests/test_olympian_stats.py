from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.test import TestCase
from django.test import Client
from django.db import connection
from ..models import Olympian
import json

class GetOlympianStatistics(TestCase):

    def setup(self):
        self.client = Client()

    def test_get_olympian_statistics(self):
        Olympian.objects.create(
            name="Tay Jimenez", sex="M", age="26", height="180", weight="61", team="Mexico", games="Summer 2016", sport="Tennis", event="Mens Singles", medal="Silver"
        )
        Olympian.objects.create(
            name="Teena Marie", sex="F", age="39", height="180", weight="30", team="Poland", games="Summer 2016", sport="Weightlifting", event="Women's Benchpress", medal="Gold"
        )
        Olympian.objects.create(
            name="Paula Abdul", sex="F", age="47", height="180", weight="61", team="Phillipines", games="Summer 2016", sport="Swimming", event="Freestly", medal="Bronze"
        )
        response = self.client.get('http://localhost:8000/api/v1/olympian_stats')
        # breakpoint()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0].__contains__('olympian_stats'), True)
        self.assertEqual(response.data[0]['olympian_stats'].__contains__('total_competing_olympians'), True)
        self.assertEqual(response.data[0]['olympian_stats'].__contains__('average_weight'), True)
        self.assertEqual(response.data[0]['olympian_stats'].__contains__('average_age'), True)
        self.assertEqual(response.data[0]['olympian_stats']['average_weight'].__contains__('unit'), True)
        self.assertEqual(response.data[0]['olympian_stats']['average_weight'].__contains__('male_olympians'), True)
        self.assertEqual(response.data[0]['olympian_stats']['average_weight'].__contains__('female_olympians'), True)
        self.assertEqual(response.data[0]['olympian_stats']['total_competing_olympians'], 3)
        self.assertEqual(response.data[0]['olympian_stats']['average_weight']['unit'], 'kg')
        self.assertEqual(response.data[0]['olympian_stats']['average_weight']['male_olympians'], 61)
        self.assertEqual(response.data[0]['olympian_stats']['average_weight']['female_olympians'], 46)
        self.assertEqual(response.data[0]['olympian_stats']['average_age'], 37)
