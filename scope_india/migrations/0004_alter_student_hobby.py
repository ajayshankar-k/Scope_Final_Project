# Generated by Django 4.2.2 on 2023-07-03 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scope_india', '0003_alter_student_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='hobby',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
