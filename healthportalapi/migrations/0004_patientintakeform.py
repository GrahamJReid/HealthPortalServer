# Generated by Django 4.1.3 on 2024-12-01 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('healthportalapi', '0003_user_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientIntakeForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('email', models.CharField(max_length=1000)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=1000)),
                ('state', models.CharField(max_length=50)),
                ('zip', models.IntegerField(max_length=1000)),
                ('phonenumber', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=1000)),
                ('birthdate', models.DateField()),
                ('socialsecurity', models.IntegerField()),
                ('emergencycontactname', models.CharField(max_length=1000)),
                ('emergencycontactphone', models.IntegerField()),
                ('patient', models.ForeignKey(db_column='patient_id', on_delete=django.db.models.deletion.CASCADE, to='healthportalapi.user')),
            ],
        ),
    ]
