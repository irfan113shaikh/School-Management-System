# Generated by Django 4.2.1 on 2023-05-30 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_student_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_feedback',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.student'),
        ),
    ]
