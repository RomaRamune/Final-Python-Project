# Generated by Django 4.1.1 on 2022-09-11 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mynotes', '0011_alter_note_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.TextField(help_text='Enter category name for your note (e.g. Important)', max_length=100, unique=True, verbose_name='Category'),
        ),
    ]