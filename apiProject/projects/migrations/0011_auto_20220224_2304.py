# Generated by Django 3.0.2 on 2022-02-24 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_rename_comment_comment_project_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]