# Generated by Django 4.2.2 on 2023-07-02 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scope_india', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
