from django.db import models, transaction


class TodoItem(models.Model):
    title = models.CharField(max_length=50)
    done = models.BooleanField()

    def __str__(self):
        return f'{self.title} [{"v" if self.done else "x"}]'

    def set_done_to_true(self):
        with transaction.atomic():
            self.done = True
            self.save()
            transaction.on_commit(self.set_name_to_done)

    def set_name_to_done(self):
        self.name = "Done"
        self.save()

