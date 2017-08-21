# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yandex_money', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='fail_url',
            field=models.URLField(default='https://boxy.store/money/fail/', verbose_name='URL неуспешной оплаты'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='scid',
            field=models.PositiveIntegerField(default='556842', verbose_name='Номер витрины'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='shop_id',
            field=models.PositiveIntegerField(default='151451', verbose_name='ID магазина'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='success_url',
            field=models.URLField(default='https://boxy.store/money/success/', verbose_name='URL успешной оплаты'),
        ),
    ]
