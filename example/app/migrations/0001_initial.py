# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yandex_money', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435')),
                ('price', models.PositiveIntegerField(verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c')),
            ],
            options={
                'verbose_name': '\u0422\u043e\u0432\u0430\u0440',
                'verbose_name_plural': '\u0422\u043e\u0432\u0430\u0440\u044b',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.PositiveIntegerField(default=1, verbose_name='\u041a\u043e\u043b-\u0432\u043e')),
                ('amount', models.PositiveIntegerField(verbose_name='\u0421\u0443\u043c\u043c\u0430 \u0437\u0430\u043a\u0430\u0437\u0430')),
                ('goods', models.ForeignKey(verbose_name='\u0422\u043e\u0432\u0430\u0440', to='app.Goods')),
                ('payment', models.ForeignKey(verbose_name='\u041f\u043b\u0430\u0442\u0435\u0436', to='yandex_money.Payment')),
            ],
            options={
                'verbose_name': '\u0417\u0430\u043a\u0430\u0437',
                'verbose_name_plural': '\u0417\u0430\u043a\u0430\u0437\u044b',
            },
        ),
    ]
