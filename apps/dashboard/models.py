from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=255)
    user_level = models.IntegerField()

class Message(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(User, related_name="sent_messages") 
    receiver = models.ForeignKey(User, related_name="messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(User, related_name="sent_comments")
    comment_message = models.ForeignKey(Message, related_name="message_comments")
