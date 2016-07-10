from __future__ import unicode_literals

from django.db import models
import json


class Repository(models.Model):
    name = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)

    def settags(self, tags):
        self.tags = json.dumps(tags)

    def gettags(self):
        return json.loads(self.tags)


class Image(models.Model):
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    digest = models.CharField(max_length=1000)
