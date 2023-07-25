from django.contrib.auth.models import User
from django.db.models import Model, CharField, TextField, TextChoices, ForeignKey, CASCADE


class Board(Model):
    name = CharField(max_length=200)

    def __str__(self):
        return self.name


class Tasks(Model):
    class TypeChoices(TextChoices):
        TODO = 'todo', 'Todo'
        DOING = 'doing', 'Doing'
        DONE = 'done', 'Done'

    title = CharField(max_length=200)
    description = TextField(blank=True, null=True)
    task_type = CharField(max_length=200, choices=TypeChoices.choices, default=TypeChoices.TODO)
    board = ForeignKey(Board, CASCADE)
    author = ForeignKey(User, CASCADE)

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title


class Subtasks(Model):
    name = CharField(max_length=200)
    task = ForeignKey(Tasks, CASCADE)


class Column(Model):
    name = CharField(max_length=200)
    board = ForeignKey(Board, CASCADE)