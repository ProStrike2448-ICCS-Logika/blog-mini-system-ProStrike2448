from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    bio = models.TextField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['name']


class Post(models.Model):
    title = models.CharField(max_length=256, unique=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.published_date} {self.title}'

    # TODO: У моделі Post, додайте метод published_recently(), який повертає True, якщо пост було опубліковано менш ніж 7 днів тому.

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-published_date']
