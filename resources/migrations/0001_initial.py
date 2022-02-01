# Generated by Django 3.0.8 on 2020-10-22 15:07

from django.db import migrations, models
import django.db.models.deletion
import resources.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('course_code', models.CharField(default='', max_length=200, primary_key=True, serialize=False)),
                ('subject', models.CharField(default='', max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FATfiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fat_paper', models.FileField(default='', null=True, upload_to=resources.models.path_and_rename_fat)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resources.Subject')),
            ],
            options={
                'verbose_name': 'FAT File',
                'verbose_name_plural': 'FAT Files',
            },
        ),
        migrations.CreateModel(
            name='CAT2files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_2', models.FileField(default='', null=True, upload_to=resources.models.path_and_rename_cat2)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resources.Subject')),
            ],
            options={
                'verbose_name': 'CAT 2 File',
                'verbose_name_plural': 'CAT 2 Files',
            },
        ),
        migrations.CreateModel(
            name='CAT1files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_1', models.FileField(default='', null=True, upload_to=resources.models.path_and_rename_cat1)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resources.Subject')),
            ],
            options={
                'verbose_name': 'CAT 1 File',
                'verbose_name_plural': 'CAT 1 Files',
            },
        ),
    ]