from django.test import TestCase
from .models import Item


class TestViews(TestCase):

    def test_get_todo_list(self):
        """ Call the url to test, check response code is 200 (all good) and
        check the template used is correct """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        """ Call the url, check response code and check template used """
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        """ Create instance of an Item, call the URL using item ID, check
        response code and template used """
        item = Item.objects.create(name='Test ToDo Item')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        """ Call url and pass in name parameter and check response URL """
        response = self.client.post('/add', {'name': 'Test Added Item'})
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        """ Create instance of item with name arguement. Call url to delete item.
        Check response URL. Create list of items with the items id and check list is
        empty """
        item = Item.objects.create(name='Test ToDo Item')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        """ Create item with name and done attibute. Call toggle URL and
        check response URL. Retrieve new item and check done attribute"""
        item = Item.objects.create(name='Test ToDo Item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)

