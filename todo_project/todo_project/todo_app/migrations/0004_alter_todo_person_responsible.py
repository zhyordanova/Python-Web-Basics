# Generated by Django 3.2.4 on 2021-06-04 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_todo_person_responsible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='person_responsible',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
