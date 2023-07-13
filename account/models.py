from django.db import models
from datetime import datetime
import statistic.models
from school.models import SchoolModel
print(statistic.models)
# Create your models here.

class PersonModel(models.Model):
    name = models.CharField(max_length=65,default='')
    fname = models.CharField(max_length=65,default='')
    date_of_birth =models.DateField(default=datetime.now)
    address = models.TextField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        abstract = True

class StudentModel(PersonModel):
    active = models.BooleanField(default=True)
    username = models.CharField(default='',max_length=25)
    password = models.CharField(default='',max_length=65)
    phone = models.CharField(default='',max_length=65)

    class Meta:
        db_table = 'student'

class TeacherModel(PersonModel):
    subject = models.ForeignKey(SubjectModel,on_delete=models.SET_NULL)
    toifa = models.CharField(max_length=65,default='')
    salary = models.PositiveIntegerField(default=1)
    school = models.ManyToManyField(to=SchoolModel)

    def __str__(self) -> str:
        return self.name