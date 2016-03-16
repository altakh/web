from django.db import models
from django.db import connection
cursor = connection.cursor()



# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(default=0)
    author = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return '/question/%d/' % self.pk
    class Meta:
        db_table = 'qaquestions'

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question, null=True)
    author = models.CharField(max_length=255)
    class Meta:
        db_table = 'qaanswers'
