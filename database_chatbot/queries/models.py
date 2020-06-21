'''
A model is the single, definitive source of information about your data. 
It contains the essential fields and behaviors of the data you’re storing. 
Generally, each model maps to a single database table.
For more info, refer to https://docs.djangoproject.com/en/3.0/topics/db/models/

'''

from django.db import models

class Query(models.Model):
    '''
    '''
    intent = models.CharField(max_length=2000)
    response = models.CharField(max_length=5530)
    
    def __str__(self):
        return 'Intent: ' + self.intent
