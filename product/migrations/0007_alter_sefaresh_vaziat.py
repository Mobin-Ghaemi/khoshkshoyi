# Generated by Django 5.0.3 on 2024-08-28 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_sefaresh_vaziat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sefaresh',
            name='vaziat',
            field=models.CharField(choices=[('1', 'اماده ی تحویل'), ('0', 'تحویل گرفته شد')], default='0', max_length=30, verbose_name='وضعیت سفارش :'),
        ),
    ]
