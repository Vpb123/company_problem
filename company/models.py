from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    megabyte_limit = 2.0
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))


class User(AbstractUser):
         pass

# Create your models here.
class Company(models.Model):
    user=models.ForeignKey('User',on_delete=models.CASCADE)
    C_name=models.CharField(max_length=50)
    Owner=models.CharField(max_length=50)
    C_type=models.CharField(max_length=30)

    def __str__(self):
        return self.C_name

class Problems(models.Model):
        company=models.ForeignKey("Company",on_delete=models.CASCADE)
        problem=models.TextField(max_length=400)
        image=models.FileField(upload_to='images/',validators=[validate_image,FileExtensionValidator(allowed_extensions=['jpeg','jpg','pdf'])], blank=True, null=True, editable=True)
        video=models.URLField( max_length=200)
        uploaded_date=models.DateField('date_added',auto_now_add=True,blank=True)

        class Meta:
                ordering=['problem']

        def __str__(self):
                return self.problem
class Student(models.Model):
        user=models.ForeignKey('User',on_delete=models.CASCADE)
        Name=models.CharField(max_length=20)
        mob_no=models.CharField(max_length=12)
        branch=models.CharField(max_length=20)
        state=models.CharField(max_length=20)
        district=models.CharField(max_length=20)
        Address=models.TextField(max_length=300)
        problems=models.ForeignKey("Problems", on_delete=models.CASCADE,blank=True,null=True)

        class Meta:
                ordering=['Name']

        def __str__(self):
            return self.Name

class Solution(models.Model):
        user=models.ForeignKey("User",on_delete=models.CASCADE)
        S_name=models.ForeignKey("Student",on_delete=models.CASCADE)
        Problem=models.ForeignKey('Problems',on_delete=models.CASCADE)
        From_date=models.DateTimeField()
        TO_date=models.DateTimeField()
        sol_name=models.CharField(max_length=10)

        def __str__(self):
                return f'{self.sol_name} -> {self.user}'

class Sol_progress(models.Model):
        sol=models.ForeignKey("Solution",on_delete=models.CASCADE)
        progress=models.IntegerField()
        progress_details=models.TextField()
        image=models.FileField(upload_to='images/',validators=[validate_image,FileExtensionValidator(allowed_extensions=['jpeg','jpg','pdf'])], blank=True, null=True, editable=True)
        video=models.URLField()

        def __str__(self):
            return self.sol
