#from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class NetworkAnalysis(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    gene_text = models.CharField(max_length=20)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#    def create_python_call(self):
#	# method to formulate software call
#	return "python %s" %(self.gene_text) 

#class AnalysisName(models.Model):
#	name=models.CharField(max_length=15)
