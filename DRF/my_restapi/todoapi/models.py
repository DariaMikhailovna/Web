from django.db import models


class TodoItem(models.Model):
    title = models.CharField(max_length=50)
    done = models.BooleanField()

    def __str__(self):
        return f'{self.title} [{"v" if self.done else "x"}]'
