# Generated by Django 4.2.3 on 2023-07-11 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scope_india', '0008_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='email',
        ),
    ]
