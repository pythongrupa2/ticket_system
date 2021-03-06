# Generated by Django 3.1.2 on 2020-10-29 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_event', models.CharField(max_length=150, verbose_name='Title of Event')),
                ('performer', models.CharField(max_length=100, verbose_name='Name of Showmans')),
                ('date_event', models.DateField()),
                ('hour_event', models.TimeField()),
                ('price_ticket', models.FloatField()),
                ('event_type', models.CharField(blank=True, max_length=15, verbose_name='Type of Event')),
            ],
        ),
    ]
