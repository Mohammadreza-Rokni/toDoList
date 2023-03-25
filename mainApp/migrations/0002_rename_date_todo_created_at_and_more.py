# Generated by Django 4.1.7 on 2023-03-25 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='Date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='Completed',
            new_name='isCompleted',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='Title',
            new_name='title',
        ),
        migrations.AddField(
            model_name='todo',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
    ]