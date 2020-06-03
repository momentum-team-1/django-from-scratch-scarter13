from django.db import models
from users.models import User

# Create your models here.
class Snippet(models.Model):
    users = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name = 'snippets')
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    description = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    #public = 

    def __str(self):
        return self.text