# Generated by Django 4.2.2 on 2023-07-02 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scope_india', '0002_alter_student_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Null', 'Select gender'), ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Null', max_length=100),
        ),
    ]
