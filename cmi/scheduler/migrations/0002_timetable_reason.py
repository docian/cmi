# Generated by Django 3.2.2 on 2021-09-18 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='reason',
            field=models.CharField(choices=[('VN', 'Vizita noua'), ('RET', 'Reteta'), ('CON', 'Consultatie'), ('OP', 'A doua opinie')], default='CON', max_length=7),
        ),
    ]