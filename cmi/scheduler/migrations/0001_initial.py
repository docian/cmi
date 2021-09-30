# Generated by Django 3.2.2 on 2021-09-30 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Ocian', max_length=30)),
                ('surname', models.CharField(default='Dan', max_length=30)),
                ('cnp', models.CharField(default='', max_length=15, unique=True)),
                ('phone', models.CharField(default='', max_length=14)),
                ('email', models.EmailField(default='', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(null=True)),
                ('duration', models.DurationField(default='00:30:00')),
                ('reason', models.CharField(choices=[('VN', 'Vizita noua'), ('RET', 'Reteta'), ('CON', 'Consultatie'), ('OP', 'A doua opinie')], default='CON', max_length=7)),
                ('pacient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.pacient')),
            ],
        ),
    ]
