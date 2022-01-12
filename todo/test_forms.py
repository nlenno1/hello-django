from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        """ Create form with empty name field, check form is_valid is false, check name is
        in the list of keys that produced errors and check the error message is correct """
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        """ Create form and check if it's valid with no Done field supplied """
        form = ItemForm({'name': 'Test ToDo Items'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        """ Create form and check the fields are named as in the list supplied """
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])


