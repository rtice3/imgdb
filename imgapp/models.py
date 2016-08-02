from __future__ import unicode_literals

from django.db import models

import os
import uuid

# Create your models here.


class UnprocessedImg(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ext = models.CharField(max_length=10, default='')
    base = models.CharField(max_length=100, default='')
    serial = models.CharField(max_length=100, default='')
    receive_date = models.DateField(auto_now_add=True)
    receive_time = models.TimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    def get_path(self):
        return os.path.join(self.base, str(self.id) + self.ext)

    def __str__(self):
        return self.serial

    def local_exists(self):
        return os.path.exists(self.get_path())


class ProcessedImg(models.Model):
    unprocessed_img = models.ForeignKey(UnprocessedImg, on_delete=models.CASCADE)
    serial = models.CharField(max_length=100, default='')
    base = models.CharField(max_length=100, default='')
    ext = models.CharField(max_length=10, default='')
    finish_date = models.DateField(auto_now_add=True)
    finish_time = models.TimeField(auto_now_add=True)

    def get_path(self):
        return os.path.join(self.base, str(self.unprocessed_img.id) + self.ext)

    def __str__(self):
        return self.unprocessed_img.serial

    def local_exists(self):
        return os.path.exists(self.get_path())

