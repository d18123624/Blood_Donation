# Generated by Django 2.1.7 on 2019-04-11 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation_requests', '0008_auto_20190410_1307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requestfordonation',
            old_name='search_match',
            new_name='search_match_donation',
        ),
    ]