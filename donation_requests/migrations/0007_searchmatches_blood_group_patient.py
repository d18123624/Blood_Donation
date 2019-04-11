# Generated by Django 2.1.7 on 2019-04-09 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation_requests', '0006_auto_20190409_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchmatches',
            name='blood_group_patient',
            field=models.CharField(choices=[('O+', 'O Positive'), ('O-', 'O Negative'), ('A+', 'A Positive'), ('A-', 'A Negative'), ('B+', 'B Positive'), ('B-', 'B Negative'), ('AB+', 'AB Positive'), ('AB-', 'AB Negative')], default='O+', max_length=2),
            preserve_default=False,
        ),
    ]
