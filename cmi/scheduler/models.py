from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import  timedelta

# Create your models here.
REASONS=(
    ("1","Vizita noua"),
    ("2","Reteta"),
    ("3","Consultatie"),
    ("4", "A doua opinie")
)

class Pacient(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    cnp = models.CharField(max_length=15, primary_key=True, db_index=False, null = False)
    phone = models.CharField(max_length=14)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name} {self.surname} {self.cnp}'

class TimeTable(models.Model):
    class VisitReason(models.TextChoices):
        NOUA='VN',_('Vizita noua')
        RETETA='RET',_('Reteta')
        CONSULT='CON',_('Consultatie')
        OPINIE='OP',_("A doua opinie")

    pacient = models.ForeignKey(Pacient, on_delete= models.CASCADE)
    time = models.DateTimeField(null=False)
    duration = models.DurationField(default="00:30:00")
    reason = models.CharField(max_length=7,choices=VisitReason.choices,default=VisitReason.CONSULT)
