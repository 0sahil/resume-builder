# Generated by Django 4.0.2 on 2022-04-12 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_alter_userdetails_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
