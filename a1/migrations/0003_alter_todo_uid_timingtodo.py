# Generated by Django 5.0.7 on 2024-12-30 05:48

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0002_alter_todo_created_at_alter_todo_uid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='TimingTodo',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('timing', models.DateTimeField()),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a1.todo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]