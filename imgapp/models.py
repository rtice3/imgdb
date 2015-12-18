from __future__ import unicode_literals

from django.db import models

import uuid

# Create your models here.


class UnprocessedImg(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    path = models.CharField(max_length=100, default='')
    serial = models.CharField(max_length=25, default='')
    receive_date = models.DateField(auto_now_add=True)
    receive_time = models.TimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)


class ProcessedImg(models.Model):
    unprocessed_img = models.ForeignKey(UnprocessedImg, on_delete=models.CASCADE)
    path = models.CharField(max_length=100, default='')
    key_path = models.CharField(max_length=100, default='')
    finish_date = models.DateField(auto_now_add=True)
    finish_time = models.TimeField(auto_now_add=True)
    processor_usage = models.DurationField()
    score = models.DecimalField(max_digits=4, decimal_places=2)

