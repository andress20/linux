from django.db import models

class TodoItem(models.Model):
    content = models.CharField(max_length=30)
    objects = models.Manager()

    def __str__(self):
        return self.content


