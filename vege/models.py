from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# from django.contrib.auth import get_user_model

# User = get_user_model() use only on view,utility 

class StudentsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,null=True,blank=True)
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField()
    recipe_view_count = models.IntegerField(default=1)
    
    
class Department(models.Model):
    department = models.CharField(max_length=100)
    
    def __str__(self):
        return self.department
    
    class Meta:
        ordering = ['department']
        
class StudentID(models.Model):
    student_id = models.CharField(max_length=100)
    
    def __str__(self):
        return self.student_id
    
class Student(models.Model):
    department= models.ForeignKey(Department, related_name="depart",on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentID,related_name="studentid",on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email  = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()
    is_deleted = models.BooleanField(default=False)
    
    objects = StudentsManager()
    admin_objects = models.Manager()
    
    def __str__(self):
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        verbose_name = "student"
        
class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.subject_name
    
class SubjectMarks(models.Model):
    student = models.ForeignKey(Student,related_name="student_marks",on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,related_name="subject",on_delete=models.CASCADE)
    marks = models.IntegerField()
    
    def __str__(self):
        return f'{self.student.student_name} {self.subject.subject_name}'
    
    class Meta:
        unique_together = ['student','subject']