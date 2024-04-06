from django.db import models

class Topic(models.Model):
    topic = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(max_length=400, null=True, blank=True)

    def serialize(self):
        return {
            'id': self.id,
            'topic': self.topic,
            'description': self.description,
        }

class UseCase(models.Model):
    topic = models.ForeignKey(Topic, related_name='use_cases', on_delete=models.CASCADE)
    description = models.TextField()

class Comparison(models.Model):
    topic1 = models.ForeignKey(Topic, related_name='comparison_as_topic1', on_delete=models.CASCADE)
    topic2 = models.ForeignKey(Topic, related_name='comparison_as_topic2', on_delete=models.CASCADE)

class ComparisonRow(models.Model):
    comparison = models.ForeignKey(Comparison, related_name='comparison_rows', on_delete=models.CASCADE)
    keyword = models.CharField(max_length=200)
    row1 = models.TextField()
    row2 = models.TextField()
    
class Tag(models.Model):
    topic = models.ManyToManyField(Topic)
    tag = models.CharField(max_length=200)

class Note(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='notes')
    content = models.TextField()