from django.db import models

# Create your models here.
class pagesapp(models.Model):
    title = models.CharField(max_length=120)
    body =models.TextField()
    author = models.CharField(max_length=100)

    def __str__ (self):
        return f"Autor:{self.author}"