# Generated by Django 2.1.7 on 2019-04-09 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_auto_20190407_2215'),
        ('donation_requests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request_For_Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('person_donation_request', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='person_donation_request', to='person.Person')),
            ],
        ),
        migrations.AlterField(
            model_name='search',
            name='search_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='person_search', to='person.Person'),
        ),
        migrations.AlterField(
            model_name='search_matches',
            name='match_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='person_match', to='donation_requests.Search'),
        ),
        migrations.AddField(
            model_name='request_for_donation',
            name='search_match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='search_match', to='donation_requests.Search_Matches'),
        ),
    ]
