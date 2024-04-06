from django.db import models

class Topic(models.Model):
    topic = models.CharField(max_length=200, null=False, blank=False)
    meaning = models.TextField(max_length=400)
    example1 = models.TextField(max_length=400, null=True, blank=True)
    example2 = models.TextField(max_length=400, null=True, blank=True)
    example3 = models.TextField(max_length=400, null=True, blank=True)

    def serialize(self):
        return {
            'id': self.id,
            'topic': self.topic,
            'meaning': self.meaning,
            'example1': self.example1,
            'example2': self.example2,
            'example3': self.example3
        }

class Tag(models.Model):
    topic = models.ManyToManyField(Topic)
    tag = models.CharField(max_length=200)
