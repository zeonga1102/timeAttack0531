from django.db import models


# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = 'category'

    name = models.CharField(max_length=256, default='')
    desc = models.CharField(max_length=256, default='')


class Article(models.Model):
    class Meta:
        db_table = 'article'

    title = models.CharField(max_length=256, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.CharField(max_length=256, default='')

