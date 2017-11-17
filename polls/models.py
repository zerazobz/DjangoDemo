import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	# """docstring for Question"""
	# def __init__(self, arg):
	# 	super(Question, self).__init__()
	# 	self.arg = arg
	def __str__(self):
		return self.question_text + " - " + self.pub_date.strftime(" %d/%m/%Y")
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	# """docstring for Choice"""
	# def __init__(self, arg):
	# 	super(Choice, self).__init__()
	# 	self.arg = arg
	# 	

	def __str__(self):
		return self.choice_text