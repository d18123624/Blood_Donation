# Generated by Django 2.1.7 on 2019-04-09 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donation_requests', '0003_auto_20190409_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchmatches',
            name='distance_in_selected_unit',
        ),
        migrations.AddField(
            model_name='searchmatches',
            name='distance_in_metres',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='searchmatches',
            name='search_criteria_met',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='searchmatches',
            name='search_match',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, related_name='search_match', to='donation_requests.Search'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='requestfordonation',
            name='search_match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='donation_search_match', to='donation_requests.SearchMatches'),
        ),
        migrations.AlterField(
            model_name='searchmatches',
            name='match_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='person_match', to='person.Person'),
        ),
    ]