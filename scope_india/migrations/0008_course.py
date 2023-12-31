# Generated by Django 4.2.3 on 2023-07-11 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scope_india', '0007_alter_student_hobby'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('image', models.FileField(upload_to='Course')),
                ('title', models.CharField(max_length=500)),
                ('duration', models.CharField(max_length=500)),
                ('fee', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Course',
            },
        ),
    ]
