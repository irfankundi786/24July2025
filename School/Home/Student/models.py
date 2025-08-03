from django.db import models
from django.utils.text import slugify


class City( models.Model):
    CITYCODE = models.IntegerField(primary_key=True)
    CITYNAME = models.TextField()
    def __str__(self):
        return f"{self.CITYCODE} - {self.CITYNAME}"
    class Meta:
        managed = False  # Django won't try to create this table
        db_table = 'CITY'  # This assumes you connected as SCOTT

class Department(models.Model):
    DEPARTMENTID = models.IntegerField(primary_key=True)
    DEPARTMENTNAME = models.TextField()
    def __str__(self):
        return f"{self.DEPARTMENTID} - {self.DEPARTMENTNAME}"
    class Meta:
        managed = False  # Django won't try to create this table
        db_table = 'DEPARTMENT'  # This assumes you connected as SCOTT

class Landrecord(models.Model):
    LANDRECORDNO = models.IntegerField(primary_key=True)
    LANDNAME = models.TextField()
    DEPARTMENTID = models.ForeignKey( Department,db_column='DEPARTMENTID',on_delete=models.SET_NULL,null=True, blank=True )
    CITYCODE = models.ForeignKey(City,db_column='CITYCODE',on_delete=models.SET_NULL,null=True,blank=True)
    AQURIEDATE = models.DateField(blank=True, null=True)
    COMMDATE = models.DateField(blank=True, null=True)
    ACQACR = models.IntegerField(blank=True, null=True)
    ACQKANAL = models.IntegerField(blank=True, null=True)
    ACQMARLA = models.IntegerField(blank=True, null=True)
    TOBEACQACR = models.IntegerField(blank=True, null=True)
    TOBEACQKANAL = models.IntegerField(blank=True, null=True)
    TOBEACQMARLA = models.IntegerField(blank=True, null=True)
    REMARKS = models.TextField(blank=True, null=True)
    PICTURE = models.ImageField(upload_to='students/', blank=True)

    def __str__(self):
        return f"{self.LANDRECORDNO} & {self.LANDNAME}"

    class Meta:
        managed = False
        db_table = 'LANDRECORD'
# Parent Model
class Parent(models.Model):
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100, blank=True)
    father_mobile = models.CharField(max_length=15)
    father_email = models.EmailField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100, blank=True)
    mother_mobile = models.CharField(max_length=15)
    mother_email = models.EmailField(max_length=100)
    present_address = models.TextField()
    permanent_address = models.TextField()

    def __str__(self):
        return f"{self.father_name} & {self.mother_name}"

# ✅ Student Model — properly placed outside Parent
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    ])
    date_of_birth = models.DateField()
    student_class = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    joining_date = models.DateField()
    mobile_number = models.CharField(max_length=15)
    admission_number = models.CharField(max_length=20)
    section = models.CharField(max_length=10)
    student_image = models.ImageField(upload_to='students/', blank=True)
    parent = models.OneToOneField(Parent, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name}-{self.last_name}-{self.student_id}")
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"
