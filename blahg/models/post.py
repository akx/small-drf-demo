from django.db import models


class Post(models.Model):
    category = models.ForeignKey("blahg.category", on_delete=models.PROTECT)
    title = models.TextField()
    content = models.TextField()
