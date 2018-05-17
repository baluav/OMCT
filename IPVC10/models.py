from django.db import models
from django.urls import reverse

# Create your models here.
class Patashala(models.Model):
    name = models.CharField(max_length=200, verbose_name='Patashala Name', help_text='Enter school name')
    address = models.CharField(max_length=200, verbose_name='Full Address', help_text='Enter door number, street name')
    city = models.CharField(max_length=50, verbose_name='City/Town', help_text='Enter locality')
    STATE_OPTIONS = (
        ('AP', 'Andhra Pradesh'),
        ('AR','Arunachal Pradesh'),
        ('AS','Assam'),
        ('BR','Bihar'),
        ('CT','Chhattisgarh'),
        ('GA','Goa'),
        ('GJ','Gujarat'),
        ('HR','Haryana'),
        ('HP','Himachal Pradesh'),
        ('JK','Jammu and Kashmir'),
        ('JH','Jharkhand'),
        ('KA','Karnataka'),
        ('KL','Kerala'),
        ('MP','Madhya Pradesh'),
        ('MH','Maharashtra'),
        ('MN','Manipur'),
        ('ML','Meghalaya'),
        ('MZ','Mizoram'),
        ('NL','Nagaland'),
        ('OR','Odisha'),
        ('PB','Punjab'),
        ('RJ','Rajasthan'),
        ('SK','Sikkim'),
        ('TN','Tamil Nadu'),
        ('TG','Telangana'),
        ('TR','Tripura'),
        ('UT','Uttarakhand'),
        ('UP','Uttar Pradesh'),
        ('WB','West Bengal'),
        ('AN','Andaman and Nicobar Islands'),
        ('CH','Chandigarh'),
        ('DN','Dadra and Nagar Haveli'),
        ('DD','Daman and Diu'),
        ('DL','Delhi'),
        ('LD','Lakshadweep'),
        ('PY','Puducherry')
    )
    state = models.CharField(max_length=50, verbose_name='State', choices=STATE_OPTIONS, help_text='Chose State')
    pincode = models.PositiveSmallIntegerField(verbose_name='Pin Code', help_text='Enter Pin Code')
    phone1 = models.CharField(max_length=20,verbose_name='Patashala Contact Number1', help_text='Enter Primary Contact Number of Patashala')
    phone2 = models.CharField(blank=True, null=True, max_length=20,verbose_name='Patashala Contact Number2', help_text='Enter Secondary Contact Number of Patashala')
    number_of_students = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Number of Students', help_text='Enter number of students in Patashala')


    def get_absolute_url(self):
        return reverse('patashala-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}'.format(self.name)

class Student(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name', help_text='Enter student''s name')
    parent_name = models.CharField(max_length=200, verbose_name='Father''s Name', help_text='Enter Student''s Father''s name')
    dob = models.DateField(null=True, blank=True, help_text='Enter in dd/mm/yyyy format')
    picture = models.ImageField(upload_to='media', blank=True, null=True)
    patashala = models.ForeignKey('Patashala',on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}'.format(self.name)

class Register(models.Model):
    dor = models.DateField(null=True, blank=True, verbose_name='Date of Registration',help_text='Enter in dd/mm/yyyy format')
    patashala = models.ForeignKey('Patashala',on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    REGISTRATION_OPTIONS = (
        ('A', 'Already Registered'),
        ('O', 'On Spot Registration')
    )
    mode = models.CharField(max_length=30, verbose_name='Registration Mode', choices=REGISTRATION_OPTIONS, help_text='Choose an option')
    comments = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('registraion-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}, {1}'.format(self.student.name, self.patashala.name)
