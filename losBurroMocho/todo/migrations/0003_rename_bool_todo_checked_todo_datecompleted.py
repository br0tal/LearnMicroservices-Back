# Generated by Django 4.1 on 2022-08-16 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_todo_datecompleted_todo_bool'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='bool',
            new_name='checked',
        ),
        migrations.AddField(
            model_name='todo',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
