# Generated by Django 4.2.3 on 2023-07-14 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scope_india', '0012_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('Course_id', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Picked',
            },
        ),
    ]
