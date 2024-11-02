# Generated by Django 5.0.3 on 2024-11-02 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0026_alter_sefaresh_vaziat'),
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
            field=models.CharField(choices=[('اماده ی تحویل', 'اماده ی تحویل'), ('تحویل مشتری داده شد', 'تحویل مشتری داده شد'), ('در حال شست و شو', 'در حال شست و شو')], default='در حال شست و شو', max_length=30, verbose_name='وضعیت سفارش:'),
        ),
    ]
