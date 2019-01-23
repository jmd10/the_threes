from django.db import models

# Create your models here.

class Topic(models.Model):
    ''' a topic to allow people to track different 'threes' ''' 
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        ''' return a string representation of the model '''
        return self.text
        
class Entry(models.Model):
    ''' journal entries for a given Topic ''' 
    
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
      ''' return a string representation of the entry. '''
      return (self.text[:50] + "..." )
            
