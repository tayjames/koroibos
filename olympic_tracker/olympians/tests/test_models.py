from django.test import TestCase
from ..models import Olympian

class OlympianTest(TestCase):

    def setUp(self):
        Olympian.objects.create(
            name="Tay Jimenez", sex="M", age="26", height="180", weight="61", team="Mexico", games="tennis", sport="Tennis", event="Mens Singles", medal="Silver"
        )

    def test_olympian(self):
        tay = Olympian.objects.get(name="Tay Jimenez")
        # breakpoint()
        self.assertEqual(tay.name, "Tay Jimenez")
        self.assertEqual(tay.sex, "M")
        self.assertEqual(tay.age, "26")
        self.assertEqual(tay.height, "180")
        self.assertEqual(tay.weight, "61")
        self.assertEqual(tay.team, "Mexico")
        self.assertEqual(tay.games, "tennis")
        self.assertEqual(tay.sport, "Tennis")
        self.assertEqual(tay.event, "Mens Singles")
        self.assertEqual(tay.medal, "Silver")
