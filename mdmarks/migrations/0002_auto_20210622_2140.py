# Generated by Django 3.2.4 on 2021-06-22 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdmarks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studental',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studenthm',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='studental',
            name='arabic_marks',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='studental',
            name='fiqh_marks',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='studental',
            name='fl_marks',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='studental',
            name='geog_marks',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='studental',
            name='hadith_marks',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='studental',
            name='hist_marks',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='studental',
            name='lst_marks',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='studental',
            name='maths_marks',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='studental',
            name='psc_marks',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='studental',
            name='sl_marks',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='studental',
            name='tafsir_marks',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='studenthm',
            name='fl_marks',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='studenthm',
            name='geog_marks',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='studenthm',
            name='hist_marks',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='studenthm',
            name='lst_marks',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='studenthm',
            name='maths_marks',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='studenthm',
            name='opt1_marks',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='studenthm',
            name='opt2_marks',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='studenthm',
            name='opt3_marks',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='studenthm',
            name='psc_marks',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='studenthm',
            name='sl_marks',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
