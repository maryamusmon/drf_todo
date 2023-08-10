# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from .models import Board, Tasks
# from .serializer import BoardModelSerializer, TaskSerializer
#
# class BoardListCreateViewTest(APITestCase):
#     def test_create_board(self):
#         url = reverse('board-list-create')
#         data = {'name': 'Test Board'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Board.objects.count(), 1)
#         self.assertEqual(Board.objects.get().name, 'Test Board')
#
#     def test_list_boards(self):
#         Board.objects.create(name='Board 1')
#         Board.objects.create(name='Board 2')
#         url = reverse('board-list-create')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 2)
#         self.assertEqual(response.data[0]['name'], 'Board 1')
#         self.assertEqual(response.data[1]['name'], 'Board 2')
#
#
# class BoardRetrieveUpdateDestroyViewTest(APITestCase):
#     def setUp(self):
#         self.board = Board.objects.create(name='Test Board')
#
#     def test_retrieve_board(self):
#         url = reverse('board-retrieve-update-destroy', kwargs={'pk': self.board.pk})
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['name'], 'Test Board')
#
#     def test_update_board(self):
#         url = reverse('board-retrieve-update-destroy', kwargs={'pk': self.board.pk})
#         data = {'name': 'Updated Board'}
#         response = self.client.put(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.board.refresh_from_db()
#         self.assertEqual(self.board.name, 'Updated Board')
#
#     def test_delete_board(self):
#         url = reverse('board-retrieve-update-destroy', kwargs={'pk': self.board.pk})
#         response = self.client.delete(url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Board.objects.count(), 0)
#
#
# class TasksRetrieveUpdateDestroyAPIViewTest(APITestCase):
#     def setUp(self):
#         self.board = Board.objects.create(name='Test Board')
#         self.task = Tasks.objects.create(title='Test Task')
#
#     def test_retrieve_task(self):
#         url = reverse('task-retrieve-update-destroy', kwargs={'pk': self.task.pk})
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['title'], 'Test Task')
#
#     def test_update_task(self):
#         url = reverse('task-retrieve-update-destroy', kwargs={'pk': self.task.pk})
#         data = {'title': 'Updated Task'}
#         response = self.client.put(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.task.refresh_from_db()
#         self.assertEqual(self.task.title, 'Updated Task')
#
#     def test_delete_task(self):
#         url = reverse('task-retrieve-update-destroy', kwargs={'pk': self.task.pk})
#         response = self.client.delete(url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Tasks.objects.count(), 0)