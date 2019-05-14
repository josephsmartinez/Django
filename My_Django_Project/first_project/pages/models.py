from django.db import models

# Create your models here.
class Topic(models.Model):
     top_name = models.CharField(max_length=264, unique=True)

     def __str__(self):
         return self.top_name
        

class Webpage(models.Model):
    # Cascade deletes. Django emulates the behavior of the SQL constraint ON 
    # DELETE CASCADE and also deletes the object containing the ForeignKey.
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=263, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)