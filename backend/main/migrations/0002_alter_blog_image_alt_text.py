# Generated by Django 4.2.1 on 2024-10-10 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image_alt_text',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
