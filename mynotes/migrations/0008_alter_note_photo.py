# Generated by Django 4.1.1 on 2022-09-09 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mynotes', '0007_note_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='covers', verbose_name='Picture'),
        ),
    ]
