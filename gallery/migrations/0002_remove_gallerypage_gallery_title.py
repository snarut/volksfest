# Generated by Django 3.2.5 on 2021-08-02 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallerypage',
            name='gallery_title',
        ),
    ]