from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=30, help_text='Title of the event.')
    date = models.DateField(help_text='Date of the event.')
    time = models.TimeField(help_text='Time of the event.')
    location = models.CharField(default='TBA', max_length=30, help_text='Location for the event.')
    event_type = models.ForeignKey('EventType', on_delete=models.SET_NULL, null=True, blank=True, help_text='Type of event')
    event_host = models.ForeignKey('EventHost', on_delete=models.SET_NULL, null=True, blank=True, help_text='Type of event')
    weblink = models.URLField(blank=True, null=True, help_text='URL to event info.')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title


class EventType(models.Model):
    name = models.CharField(unique=True, max_length=20, help_text='Name of the event type.')
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class EventHost(models.Model):
    name = models.CharField(unique=True, max_length=20, help_text='Name of the events host.')
    weblink = models.URLField(blank=True, null=True, help_text='URL to host info.')

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name