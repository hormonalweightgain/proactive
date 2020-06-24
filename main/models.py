from django.db import models

# Create your models here.
PURPOSE_CHOICES= (
    ('GW','I want to know why I might have gained weight'),
    ('FR','I am more concerned about future risks from this weight gain '),
    ('BC','Want to prepare my body for conception'),
    ('PR','Need to get my prescription renewed'),
    ('SO','Need to get a second opinion'),
    ('PC','Follow up for previous consultation'),
    ('other','Other')
)
HAVE_BABY_CHOICES=(
    ('y','yes'),
    ('n','no'),
)

MONTH8_CHOICES=(
    ('JAN','JAN'),
    ('FEB','FEB'),
    ('MAR','MAR'),
    ('APR','APR'),
    ('MAY','MAY'),
    ('JUN','JUN'),
    ('JUL','JUL'),
    ('AUG','AUG'),
    ('SEP','SEP'),
    ('OCT','OCT'),
    ('NOV','NOV'),
    ('DEC','DEC'),
)

YEAR8_CHOICES=(
    ('2019','2019'),
    ('2020','2020'),
)

TIME9_D_CHOICES=(
    ('d','days'),
    ('m','months'),
    ('y','years')
)
class Patient(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    dob=models.DateField(default="2020-06-02")
    weight=models.IntegerField(default="50")
    waist=models.IntegerField(default="28")
    hip=models.IntegerField(default="30")
    purpose=models.CharField(max_length=100, choices=PURPOSE_CHOICES, default='GW')
    have_baby=models.CharField(max_length=100,choices=HAVE_BABY_CHOICES,default='n')
    hyperprolactinemia=models.CharField(max_length=100,default='not_there',null=True,blank=True)
    pcos_pcod=models.CharField(max_length=100,default='not_there',null=True,blank=True)
    hypothyroidism=models.CharField(max_length=100,default='not_there',null=True,blank=True)
    other=models.CharField(max_length=100,default='not_there',null=True,blank=True)
    hyperprolactinemia_days=models.IntegerField(null=True,blank=True,default=0)
    pcos_pcod_days=models.IntegerField(null=True,blank=True,default=0)
    hypothyroidism_days=models.IntegerField(null=True,blank=True,default=0)
    other_days=models.IntegerField(null=True,blank=True,default=0)
    symptoms7=models.CharField(max_length=100,default="none")
    month8=models.CharField(max_length=100,choices=MONTH8_CHOICES,default='JAN')
    year8=models.CharField(max_length=100,choices=YEAR8_CHOICES,default='2019')
    weight9=models.IntegerField(null=True,blank=True,default=None)
    time9=models.IntegerField(null=True,blank=True,default=None)
    time9_d=models.CharField(max_length=100,choices=TIME9_D_CHOICES,default='m')
    
    
    
    
    


