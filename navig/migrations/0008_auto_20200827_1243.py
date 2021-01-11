# Generated by Django 3.1 on 2020-08-27 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navig', '0007_gitandvsc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socket',
            old_name='client',
            new_name='file2',
        ),
        migrations.RemoveField(
            model_name='gitandvsc',
            name='md',
        ),
        migrations.RemoveField(
            model_name='socket',
            name='server',
        ),
        migrations.AddField(
            model_name='gitandvsc',
            name='file1',
            field=models.CharField(default=0, max_length=10000),
        ),
        migrations.AddField(
            model_name='gitandvsc',
            name='name1',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='socket',
            name='name1',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='socket',
            name='name2',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='gitandvsc',
            name='vid',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AlterField(
            model_name='socket',
            name='vid',
            field=models.CharField(default=0, max_length=500),
        ),
    ]