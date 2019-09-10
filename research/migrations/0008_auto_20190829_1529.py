# Generated by Django 2.2.4 on 2019-08-29 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0007_auto_20190828_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('head', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='heads', to='research.Event')),
                ('tail', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tails', to='research.Event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='relationships',
            field=models.ManyToManyField(blank=True, to='research.Relationship'),
        ),
    ]