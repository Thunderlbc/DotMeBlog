from django.db import models

# Create your models here.


class Articles(models.Model):

    title = models.CharField(max_length=100)    #Title
    category = models.CharField(max_length=50, blank=True)
    date_time = models.DateField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title


    class Meta:
        ordering=['-date_time']
