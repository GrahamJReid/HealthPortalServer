# Generated by Django 4.1.3 on 2024-11-24 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthportalapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='patient', max_length=100),
            preserve_default=False,
        ),
    ]
