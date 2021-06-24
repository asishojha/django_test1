# Generated by Django 3.2.4 on 2021-06-23 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdmarks', '0011_auto_20210624_0138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studental',
            name='arabic',
        ),
        migrations.RemoveField(
            model_name='studental',
            name='geog',
        ),
        migrations.RemoveField(
            model_name='studental',
            name='hist',
        ),
        migrations.RemoveField(
            model_name='studental',
            name='lsc',
        ),
        migrations.RemoveField(
            model_name='studental',
            name='psc',
        ),
        migrations.RemoveField(
            model_name='studenthm',
            name='arabic',
        ),
        migrations.RemoveField(
            model_name='studenthm',
            name='geog',
        ),
        migrations.RemoveField(
            model_name='studenthm',
            name='hist',
        ),
        migrations.RemoveField(
            model_name='studenthm',
            name='lsc',
        ),
        migrations.RemoveField(
            model_name='studenthm',
            name='psc',
        ),
        migrations.AddField(
            model_name='studental',
            name='arabic_marks',
            field=models.CharField(max_length=3, null=True, verbose_name='Arabic'),
        ),
        migrations.AddField(
            model_name='studental',
            name='geog_marks',
            field=models.CharField(max_length=2, null=True, verbose_name='Geography'),
        ),
        migrations.AddField(
            model_name='studental',
            name='hist_marks',
            field=models.CharField(max_length=3, null=True, verbose_name='History'),
        ),
        migrations.AddField(
            model_name='studental',
            name='lsc_marks',
            field=models.CharField(max_length=2, null=True, verbose_name='Life Science'),
        ),
        migrations.AddField(
            model_name='studental',
            name='psc_marks',
            field=models.CharField(max_length=2, null=True, verbose_name='Physical Science'),
        ),
        migrations.AddField(
            model_name='studenthm',
            name='arabic_marks',
            field=models.CharField(max_length=3, null=True, verbose_name='Arabic'),
        ),
        migrations.AddField(
            model_name='studenthm',
            name='geog_marks',
            field=models.CharField(max_length=2, null=True, verbose_name='Geography'),
        ),
        migrations.AddField(
            model_name='studenthm',
            name='hist_marks',
            field=models.CharField(max_length=3, null=True, verbose_name='History'),
        ),
        migrations.AddField(
            model_name='studenthm',
            name='lsc_marks',
            field=models.CharField(max_length=2, null=True, verbose_name='Life Science'),
        ),
        migrations.AddField(
            model_name='studenthm',
            name='psc_marks',
            field=models.CharField(max_length=2, null=True, verbose_name='Physical Science'),
        ),
    ]
