# Generated by Django 2.1.7 on 2019-04-07 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='email',
        ),
    ]