# Generated by Django 3.2.16 on 2022-11-20 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hemo', '0002_auto_20221120_2201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hemo',
            old_name='geometria',
            new_name='geometry',
        ),
    ]
