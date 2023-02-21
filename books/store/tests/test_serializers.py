from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Book, UserBookRelation
from store.serializer import BookSerializer


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        user1 = User.objects.create(username='user1')
        user2 = User.objects.create(username='user2')
        user3 = User.objects.create(username='user3')

        book_1 = Book.objects.create(name='Test Book 1', price=25, author_name='Author 1')
        book_2 = Book.objects.create(name='Test Book 2', price=55, author_name='Author 2')

        UserBookRelation.objects.create(user=user1, book=book_1, like=True)
        UserBookRelation.objects.create(user=user2, book=book_1, like=True)
        UserBookRelation.objects.create(user=user3, book=book_1, like=True)

        data = BookSerializer([book_1, book_2], many=True).data
        exepted_data = [
            {
                'id': book_1.id,
                'name': 'Test Book 1',
                'price': '25.00',
                'author_name': 'Author 1',
                'likes_count': 0
            },
            {
                'id': book_2.id,
                'name': 'Test Book 2',
                'price': '55.00',
                'author_name': 'Author 2',
                'likes_count': 0
            },
        ]
        self.assertEqual(exepted_data, data)
