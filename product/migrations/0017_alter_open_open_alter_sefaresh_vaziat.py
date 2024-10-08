# Generated by Django 5.0.3 on 2024-08-29 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_alter_sefaresh_vaziat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='open',
            name='open',
            field=models.CharField(choices=[('باز', 'باز'), ('بسته', 'بسته')], max_length=25, verbose_name='وضعیت باز بودن : '),
        ),
        migrations.AlterField(
            model_name='sefaresh',
            name='vaziat',
            field=models.CharField(choices=[('تحویل مشتری داده شد', 'تحویل مشتری داده شد '), ('در حال شست و شو ', 'در حال شست و شو'), ('اماده ی تحویل', 'اماده ی تحویل')], default='در حال شست و شو', max_length=30, verbose_name='وضعیت سفارش :'),
        ),
    ]
