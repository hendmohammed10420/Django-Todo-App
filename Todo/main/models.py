from django.db import models
import datetime

# Create your models here.
class Todo(models.Model):
    # gradechoices=[
    #     ('A+','100'),
    #     ('B+','85'),
    #     ('C+','75'),
    # ]
    # grade=models.CharField(max_length=2,choices=gradechoices,null=True,blank=True)
    
    # description=models.TextField()
    # email=models.EmailField()
    # image=models.ImageField()
    name=models.CharField(max_length=150)
    createdAt=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    is_completed=models.BooleanField(default=False)
     
    def __str__(self):
         return self.name 
     
    def getdesc(self):
        return self.description[:50] +'....'


# ----------------------------------------------------------
class TodoItems(models.Model):
      name=models.CharField(max_length=150, null=True,blank=True)
      createdAt=models.DateTimeField(auto_now_add=True)
      description=models.TextField(null=True,blank=True)
      is_completed=models.BooleanField(default=False)
      todo = models.ForeignKey(Todo,on_delete=models.SET_NULL,null=True)  

      def __str__(self):
          return self.name 