# Generated by Django 3.1 on 2020-09-01 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navig', '0010_pygame'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ied', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=20)),
                ('did', models.CharField(max_length=4)),
            ],
        ),
    ]
