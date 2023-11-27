from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

position_choices=[
('center','center'),
('roadside','roadside'),
]
status_choices=[
('work in progress','work in progress'),
('repaired','repaired'),
('temporary repair','temporary repair'),
('not repair','not repair'),
]

class Worker(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    status=models.BooleanField(default=True)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id




class Citizen(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    admitDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id

class Hole(models.Model):
    street=models.CharField(max_length=30)
    size = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    position=models.CharField(max_length=30,choices=position_choices)
    area=models.CharField(max_length=30)
    priority=models.PositiveIntegerField(null=True)
    status=models.CharField(max_length=30,choices=status_choices,default='not repair')










