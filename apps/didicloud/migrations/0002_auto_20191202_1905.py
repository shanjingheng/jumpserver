# Generated by Django 2.1.7 on 2019-12-02 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('didicloud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dc2',
            name='cpu',
            field=models.IntegerField(default=0, verbose_name='Cpu'),
        ),
        migrations.AddField(
            model_name='dc2',
            name='memory',
            field=models.IntegerField(default=0, verbose_name='Memory'),
        ),
    ]
