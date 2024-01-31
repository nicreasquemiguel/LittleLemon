from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_create_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)

    def test_getall(self):
        all = Menu.objects.all()
        self.assertEqual(str(all[0]), "IceCream : 80.0")