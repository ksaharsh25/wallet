# Generated by Django 4.1.4 on 2022-12-20 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0005_alter_person_chemistry_alter_person_english_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='marks',
        ),
    ]
