# Generated by Django 4.1.4 on 2022-12-20 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_alter_person_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='chemistry',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='english',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='maths',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='physics',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
    ]
