# Generated by Django 2.1.15 on 2020-03-20 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200320_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='delivers',
            field=models.CharField(choices=[('DELIVERY', 'Delivery'), ('TAKEOUT', 'TakeOut')], default='TAKEOUT', max_length=10),
        ),
    ]
