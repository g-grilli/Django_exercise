import datetime
from django.db import models
from django.utils import timezone

class Catagory(models.Model):
  name = models.CharField(max_length=50)
  slug = models.SlugField(max_length=50, unique=True)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    catagories = models.ManyToManyField(Catagory)
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):        
    	return self.choice_text
