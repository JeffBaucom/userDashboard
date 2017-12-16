from __future__ import unicode_literals
from django.db import models
import bcrypt
# Managers
class UserManager(models.Manager):

    # method for inserting a user
    def registration_validator(self, postData):
        errors = {}
        #TODO add validations
        first_name = postData['first_name']
        last_name = postData['last_name']
        email = postData['email']
        password = postData['password']
        confirm = postData['cPassword']
        if not errors:
            hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password, user_level=user_level)
            return errors

class User(models.Model):
    email = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=255)
    user_level = models.IntegerField()

    objects = UserManager()

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

    objects = UserManager()
