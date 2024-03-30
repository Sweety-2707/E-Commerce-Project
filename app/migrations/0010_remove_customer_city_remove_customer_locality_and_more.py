# Generated by Django 4.2.2 on 2023-07-17 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_customer_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='city',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='locality',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='state',
        ),
        migrations.CreateModel(
            name='Delivery_Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('state', models.CharField(choices=[('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Arunanchal Pradesh', 'Arunanchal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chandigarh', 'Chandigarh'), ('Chhatisgarh', 'Chhatisgarh'), ('Dadar & Nagar Haveli', 'Dadar & Nagar Haveli'), ('Daman & Diu', 'Daman & Diu'), ('Delhi', 'Delhi'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Lakshadweep', 'Lakshadweep'), ('Ladhak', 'Ladhak'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Puducherry', 'Puducherry'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttarakhand', 'Uttarakhand'), ('Uttar Pradesh', 'Uttar Pradesh'), ('West Bengal', 'West Bengal')], max_length=50)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
            ],
        ),
    ]