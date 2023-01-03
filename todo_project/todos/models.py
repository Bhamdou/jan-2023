from django.db import models

## Some more fields !!
## completed or done or finito! (Boolean field)
## 20 minutes

## Extra work: Add a checkbox or radio to the form 
## to inform the user of the application that a TODO is completed.

# Create your models here.
# class Todo(models.Model):
#     description = models.TextField()

#     def __str__(self):
#         return self.description
    

class Todo(models.Model):
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"description: {self.description},completed: {self.completed}"

