from django.db import models

# Create your models here.
class Todo(models.Model):
    """This class defines a Todo model with two fields representing the text in the todo list & a complete field representing the task whether it is complete or not. 
    It is set false by default.
    Returns:
        return text as representation of todo
    """
    text=models.CharField(max_length=40)
    complete=models.BooleanField(default=False)

    def __str__(self):
        return self.text
