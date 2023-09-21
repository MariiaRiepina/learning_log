from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)  # Fixed typo ("Charfield" to "CharField")
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):  # Corrected the indentation of the method
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) <= 50:
            return self.text
        else:
            return self.text[:50] + "..."


class Locations(models.Model):
    """Specified a locations"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_locations')
    parent_location = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    hierarchy_level = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, default='')

    USERNAME_FIELD = 'username'

    def __str__(self):
       return self.user.username
