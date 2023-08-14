# import pytest
# from rest_framework import status
# from rest_framework.reverse import reverse
# from rest_framework.test import APIClient
#
# from tasks.views import TaskCreateAPIView
# from users.models import User
#
#
# # BoardListCreateAPIView
# @pytest.mark.django_db
# def test_create_board_with_columns():
#     user = User.objects.create_user(username='testuser', password='testpassword')
#     client = APIClient()
#     client.force_authenticate(user=user)
#
#     url = reverse('board')
#
#     data = {
#         'name': 'Test Board',
#         'columns': ['Column 1', 'Column 2']
#     }
#
#     response = client.post(url, data, format='multipart')
#
#     assert response.status_code == status.HTTP_201_CREATED
#     assert 'id' in response.data
#     assert 'columns' in response.data
#
#
# @pytest.mark.django_db
# def test_create_board_without_columns():
#     user = User.objects.create_user(username='testuser', password='testpassword')
#     client = APIClient()
#     client.force_authenticate(user=user)
#
#     url = reverse('board')
#
#     data = {
#         'name': 'Test Board'
#     }
#
#     response = client.post(url, data, format='multipart')
#
#     assert response.status_code == status.HTTP_201_CREATED
#     assert 'id' in response.data
#     assert 'columns' not in response.data
#
#
# # TaskCreateAPIView
#
# @pytest.mark.django_db
# def test_create_task_with_subtasks_and_author():
#     user = User.objects.create_user(username='testuser', password='testpassword')
#     client = APIClient()
#     client.force_authenticate(user=user)
#
#     url = reverse('task')
#
#     data = {
#         'name': 'Test Task',
#         'subtasks': ['Subtask 1', 'Subtask 2'],
#         'author': [user.email]
#     }
#
#     response = client.post(url, data, format='multipart')
#
#     assert response.status_code == status.HTTP_201_CREATED
#     assert 'id' in response.data
#     assert 'subtasks' in response.data
#     assert 'author' in response.data
#
#
# @pytest.mark.django_db
# def test_create_task_without_subtasks_and_author():
#     user = User.objects.create_user(username='testuser', password='testpassword')
#     client = APIClient()
#     client.force_authenticate(user=user)
#
#     view = TaskCreateAPIView.as_view(actions={'post': 'create'})
#
#     url = reverse('task')
#
#     data = {
#         'name': 'Test Task'
#     }
#
#     response = client.post(url, data, format='multipart')
#
#     assert response.status_code == status.HTTP_201_CREATED
#     assert 'id' in response.data
#     assert 'subtasks' not in response.data
#     assert 'author' not in response.data
