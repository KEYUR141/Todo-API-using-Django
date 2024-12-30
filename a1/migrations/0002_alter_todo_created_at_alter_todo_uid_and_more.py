# Generated by Django 5.0.7 on 2024-12-16 10:59

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('a2065bb0-fdfa-4f09-a4f2-3781c6e64366'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
