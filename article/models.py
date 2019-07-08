from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=50)
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
