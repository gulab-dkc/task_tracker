# Generated by Django 5.1.5 on 2025-04-11 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='finishedtask',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
