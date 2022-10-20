from django.test import TestCase
from .models import Item

# Create your tests here.


class TestViews(TestCase):
    def test_get_to_do_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('to_do_list.html')

    def test_get_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('add_item.html')

    def test_get_edit_item_page(self):
        item = Item.objects.create(name='Testing to do item')
        response = self.client.get(f'/edit/{ item.id }')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('edit_item.html')

    def test_add_item(self):
        response = self.client.post('/add', {'name': 'New testing item'})
        self.assertRedirects(response, '/')
    
    def test_delete_item(self):
        item = Item.objects.create(name='Testing to do item')
        response = self.client.get(f'/delete/{ item.id }')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle(self):
        item = Item.objects.create(name='Testing to do item', done=True)
        response = self.client.get(f'/toggle/{ item.id }')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)
