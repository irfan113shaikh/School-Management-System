# Generated by Django 4.2.1 on 2023-05-30 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_student_feedback_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_feedback',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
