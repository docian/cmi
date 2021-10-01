from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import  timedelta

# Create your models here.
from pygments.lexer import default

REASONS=(
    ("1","Vizita noua"),
    ("2","Reteta"),
    ("3","Consultatie"),
    ("4", "A doua opinie")
)

class Pacient(models.Model):
    name = models.CharField(max_length=30, null=False, default='Ocian')
    surname = models.CharField(max_length=30, null=False, default='Dan')
    cnp = models.CharField(max_length=15, unique=True, null = False, default='')
    phone = models.CharField(max_length=14, default='')
    email = models.EmailField(default='')

    def __str__(self):
        return f'{self.name} {self.surname} {self.cnp}'

class TimeTable(models.Model):
    class VisitReason(models.TextChoices):
        NOUA='VN',_('Vizita noua')
        RETETA='RET',_('Reteta')
        CONSULT='CON',_('Consultatie')
        OPINIE='OP',_("A doua opinie")

    pacient = models.ForeignKey(Pacient, on_delete= models.CASCADE)
    time = models.DateTimeField(null=True)
    duration = models.DurationField(default="00:30:00")
    reason = models.CharField(max_length=7,choices=VisitReason.choices,default=VisitReason.CONSULT)
