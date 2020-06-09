from django.db import models
from users.models import User

# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag


class Snippet(models.Model):
    PUBLIC = 'PUB'
    PRIVATE = 'PRI'
    VISIBILITY_CHOICES =[
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
    ]
    user = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name = 'snippets')
    title = models.CharField(max_length=255, null=True, blank=True)
    #date = models.DateField(auto_now_add=True, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(to=Tag, related_name='snippets')
    visibility = models.CharField(max_length=3, choices=VISIBILITY_CHOICES, default=PRIVATE)

    def get_tag_names(self):
        tag_names = []
        for tag in self.tags.all():
            tag_names.append(tag.tag)
        return " ".join(tag_names)

    def set_tag_names(self, tag_names):
        tag_names = tag_names.split()
        tags = []
        for tag_name in tag_names:
            tag = Tag.objects.filter(tag=tag_name).first()
            if tag is None:
                tag = Tag.objects.create(tag=tag_name)
            tags.append(tag)
        self.tags.set(tags)

    def __str__(self):
        return self.title

