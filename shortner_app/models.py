from django.db import models


# Create your models here.
from shortner_app.utils import generate_random_alias


class UrlShort(models.Model):
    alias = models.CharField(max_length=8, default=generate_random_alias, primary_key=True)
    url = models.URLField()
