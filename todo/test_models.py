from django.test import TestCase
from .models import Item


class TextModel(TestCase):

    def test_done_default_to_false(self):
        item = Item.objects.create(name='Test ToDo Item')
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name='Test ToDo Item')
        self.assertEqual(str(item), 'Test ToDo Item')