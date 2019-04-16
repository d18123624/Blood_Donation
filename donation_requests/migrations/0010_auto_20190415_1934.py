# Generated by Django 2.1.7 on 2019-04-15 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation_requests', '0009_auto_20190411_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='blood_group_patient',
            field=models.CharField(choices=[('O+', 'O Positive'), ('O-', 'O Negative'), ('A+', 'A Positive'), ('A-', 'A Negative'), ('B+', 'B Positive'), ('B-', 'B Negative'), ('AB+', 'AB Positive'), ('AB-', 'AB Negative')], max_length=3),
        ),
    ]