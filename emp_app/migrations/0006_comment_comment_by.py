# Generated by Django 5.2 on 2025-04-14 07:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0005_remove_task_assigned_to_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
