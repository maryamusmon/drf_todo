from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline

from tasks.models import Tasks, Subtasks, Board, Column


# Register your models here.

class TasksInline(StackedInline):
    model = Subtasks
    max_num = 4
    fields = ('name',)


@admin.register(Tasks)
class ProductsModelAdmin(ModelAdmin):
    inlines = [TasksInline]


class BoardInline(StackedInline):
    model = Column
    max_num = 4
    fields = ('name',)


@admin.register(Board)
class BoardModelAdmin(ModelAdmin):
    inlines = [BoardInline]
