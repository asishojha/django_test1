# Generated by Django 3.2.4 on 2021-06-22 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdmarks', '0002_auto_20210622_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studental',
            name='addl',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='studental',
            name='sl',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='studenthm',
            name='addl',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='studenthm',
            name='sl',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
