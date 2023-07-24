from django.contrib import admin
from django.contrib.admin import ModelAdmin

from tasks.models import Tasks, Subtasks, Board


# Register your models here.

class TasksInline(admin.StackedInline):
    model = Subtasks
    max_num = 4
    fields = ('name',)


@admin.register(Tasks)
class ProductsModelAdmin(ModelAdmin):
    inlines = [TasksInline]

@admin.register(Board)
class BoardModelAdmin(ModelAdmin):
    pass

