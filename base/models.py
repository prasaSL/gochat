from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User model with additional fields
class User(AbstractUser):
    name = models.CharField(max_length=200 , null=True)
    email = models.EmailField(null=True , unique=True)
    bio = models.TextField(null=True)

    avatar=models.ImageField(null=True, default='avatar.svg')

# Use email as the username field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


# Topic model for categorizing rooms
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Room model for chat rooms
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']
    def __str__(self):
        return self.name
    

# Message model for chat messages in rooms
class Message(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   room = models.ForeignKey(Room, on_delete=models.CASCADE)
   body = models.TextField()
   updated = models.DateTimeField(auto_now=True)
   created = models.DateTimeField(auto_now_add=True)
   class Meta:
        ordering = ['-updated','-created']
   
   def __str__(self):
        return self.body[0:50]