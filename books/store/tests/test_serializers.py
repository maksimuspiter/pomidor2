from django.test import TestCase

from store.models import Book
from store.serializer import BookSerializer


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name='Test Book 1', price=25)
        book_2 = Book.objects.create(name='Test Book 2', price=55)
        data = BookSerializer([book_1, book_2], many=True).data
        exepted_data = [
            {
                'id': book_1.id,
                'name': 'Test Book 1',
                'price': '25.00'
            },
            {
                'id': book_2.id,
                'name': 'Test Book 2',
                'price': '55.00'
            }
        ]
        print(exepted_data)
        print('****************************************************************')
        print(data)
        self.assertEqual(exepted_data, data)