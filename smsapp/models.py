from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class StudentModel(models.Model):
	rno=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=40)
	marks=models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])

	def __str__(self):
		return str(self.rno) +" "+ str(self.name) +" "+str(self.marks)

