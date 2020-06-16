# Generated by Django 3.0.7 on 2020-06-16 10:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0002_auto_20200615_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('web', 'web'), ('mobile', 'mobile')], default='web', max_length=2048),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=2048),
        ),
        migrations.AlterField(
            model_name='saleactivity',
            name='days',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]