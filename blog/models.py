from django.db import models

# Create your models here.

class Writer(models.Model):
   name = models.CharField(max_length=50)

   def __str__(self):
      return self.name

class Blog(models.Model):
   title = models.CharField(max_length=100)
   sub_heading = models.CharField(max_length=300)
   content= models.TextField(max_length=5000)
   date_of_publish = models.DateField(auto_now_add=True)   
   writer = models.ForeignKey(Writer, on_delete=models.SET_NULL, null=True)
   updated_on = models.DateTimeField(auto_now= True)

   class Meta:
      ordering = ['-date_of_publish']

   def __str__(self):
      return self.title

