from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Queue(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Queue, self).save(*args, **kwargs)
    def __str__(self):
        return self.name

class Member(models.Model):
    full_name = models.CharField(max_length=200)
    pin = models.IntegerField()
    def __str__(self):
        return self.full_name

class QueueMember(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    queue = models.ForeignKey(Queue, on_delete=models.CASCADE)
    added_at = models.DateTimeField(default=timezone.now)
    outcome_id = models.ForeignKey('Outcome', on_delete=models.SET_NULL, blank=True, null=True)
    outcome_notes = models.TextField(blank=True, null=True)
    resolved_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.member.full_name + " -- " + self.queue.name

class Outcome(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name