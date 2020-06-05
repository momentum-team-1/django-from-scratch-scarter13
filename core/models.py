from django.db import models
from users.models import User

# Create your models here.
class Snippet(models.Model):
    user = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name = 'snippets')
    title = models.CharField(max_length=255, null=True, blank=True)
    #date = models.DateField(auto_now_add=True, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.text