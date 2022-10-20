from django.test import TestCase
from .models import Item

# Create your tests here.


class TestModels(TestCase):
    def test_default_done_status(self):
        item = Item.objects.create(name='third test item')
        self.assertFalse(item.done)

    def test_string_method(self):
        item = Item.objects.create(name='third test item')
        self.assertEqual(str(item), 'third test item')
