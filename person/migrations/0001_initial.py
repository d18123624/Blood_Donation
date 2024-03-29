# Generated by Django 2.1.7 on 2019-04-07 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('age', models.SmallIntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1)),
                ('blood_group', models.CharField(choices=[('O+', 'O Positive'), ('O-', 'O Negative'), ('A+', 'A Positive'), ('A-', 'A Negative'), ('B+', 'B Positive'), ('B-', 'B Negative'), ('AB+', 'AB Positive'), ('AB-', 'AB Negative')], max_length=2)),
                ('address_lat', models.DecimalField(decimal_places=16, max_digits=22)),
                ('address_long', models.DecimalField(decimal_places=16, max_digits=22)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('mobile_number', models.DecimalField(decimal_places=0, max_digits=13)),
                ('last_blood_donation', models.DateTimeField(blank=True, null=True)),
                ('currently_eligible_for_donation', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
