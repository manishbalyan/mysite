from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date publised')

	def __str__(self):
		return self.question_text

	def was_publised_recentely(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text