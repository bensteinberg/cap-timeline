# Generated by Django 2.2.4 on 2019-09-10 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0009_auto_20190909_1727'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='tags',
            new_name='groups',
        ),
    ]
