#from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.forms import ModelForm

LOCATIONS = (  
    ('BRO', 'Bronx'),
    ('BRK', 'Brooklyn'),
    ('QNS', 'Queens'),
    ('MAN', 'Manhattan'),
    ('STN', 'Staten Island'),
)

class NetworkAnalysis(models.Model):
    author = models.ForeignKey('auth.User')
    email = models.EmailField()
    analysis_title = models.CharField(max_length=200)
    analysis_description = models.TextField()
    gene_target = models.CharField(max_length=20)
    created_date = models.DateTimeField(
            )#initial=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    # New things that will be relevant parameters for the algorithm
    threshold = models.DecimalField('threshold',max_digits=4,decimal_places=2)
    eQTL = models.BooleanField('Include eQTL predictions?',default=True)
    location = models.CharField(max_length=3, choices=LOCATIONS)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

