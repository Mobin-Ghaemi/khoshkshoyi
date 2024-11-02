# Generated by Django 4.2 on 2024-10-02 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_sefaresh_tedad_alter_open_open_alter_sefaresh_vaziat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sefaresh',
            name='vaziat',
            field=models.CharField(choices=[('تحویل مشتری داده شد', 'تحویل مشتری داده شد'), ('در حال شست و شو', 'در حال شست و شو'), ('اماده ی تحویل', 'اماده ی تحویل')], default='در حال شست و شو', max_length=30, verbose_name='وضعیت سفارش:'),
        ),
    ]