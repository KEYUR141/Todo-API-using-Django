# Generated by Django 5.0.7 on 2024-12-30 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0003_alter_todo_uid_timingtodo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timingtodo',
            name='timing',
            field=models.DateField(),
        ),
    ]