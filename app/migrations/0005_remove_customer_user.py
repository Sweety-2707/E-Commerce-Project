# Generated by Django 4.2.2 on 2023-07-08 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_customer_cpassword_customer_email_customer_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]
