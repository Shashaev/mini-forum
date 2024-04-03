from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
