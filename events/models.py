from django.db import models
from common.models import mentor,company

class Event(models.Model):
    event_id = models.CharField(max_length=50)
    title= models.CharField(max_length=100,null=True)
    location = models.CharField(max_length=100,null=True)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    join_link = models.URLField()
    category = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to='static/events',null=True)
    mentor = models.ForeignKey(mentor, on_delete=models.CASCADE)
    company = models.ForeignKey(company, on_delete=models.CASCADE)

    def __str__(self):
        return self.event_id

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class RSVP(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.candidate.name} - {self.event.event_id}"