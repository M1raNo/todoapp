# Generated by Django 3.2.9 on 2021-11-30 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='time',
            field=models.DateField(auto_now_add=True),
        ),
    ]
