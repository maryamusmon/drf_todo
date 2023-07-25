from django.contrib.auth.models import User
from django.db.models import Model, CharField, TextField, ForeignKey, CASCADE, BooleanField


class Board(Model):
    name = CharField(max_length=200)

    def __str__(self):
        return self.name


class Column(Model):
    name = CharField(max_length=200)
    board = ForeignKey(Board, CASCADE)


class Tasks(Model):
    title = CharField(max_length=200)
    description = TextField(blank=True, null=True)

    status = ForeignKey(Column, CASCADE)

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title


class Subtasks(Model):
    name = CharField(max_length=200)
    is_completed = BooleanField(default=False)
    task = ForeignKey(Tasks, CASCADE)
