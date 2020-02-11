from django.conf import settings
from django.db import models
from django.utils import timezone

class Queue(models.Model):
    name = models.CharField(max_length=200)

class Member(models.Model):
    full_name = models.CharField(max_length=200)
    pin = models.IntegerField()

class QueueMember(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    queue = models.ForeignKey(Queue, on_delete=models.CASCADE)
    added_at = models.DateTimeField(default=timezone.now)
    outcome_id = models.ForeignKey('Outcome', on_delete=models.SET_NULL, null=True)
    outcome_notes = models.TextField()
    resolved_at = models.DateTimeField(default=timezone.now)

class Outcome(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()