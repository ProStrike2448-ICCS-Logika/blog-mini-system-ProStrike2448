from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=256, unique=True)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.published_date} {self.title}'

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-published_date']
