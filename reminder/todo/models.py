from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    description=models.TextField(max_length=200,null=True)
    def __str__(self) -> str:
        return self.category_name
class Task(models.Model):
    class Priority(models.IntegerChoices):
        HIGH = 1
        MEDIUM = 2
        LOW = 3
    title=models.CharField(db_column="Title" ,max_length=200)
    description=models.TextField(db_column="Description",max_length=200)
    category = models.ManyToManyField('Category')
    priority=models.IntegerField(choices=Priority.choices)
    create_time = models.DateTimeField(auto_now_add=True)
    time = models.DateTimeField()

    def __str__(self) -> str:
        return self.title
# Create your models here.

