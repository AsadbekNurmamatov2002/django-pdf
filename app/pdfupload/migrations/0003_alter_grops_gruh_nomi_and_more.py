# Generated by Django 5.0.6 on 2024-06-03 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfupload', '0002_alter_grops_fakulteti'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grops',
            name='gruh_nomi',
            field=models.CharField(max_length=200, verbose_name='Guruh nomi'),
        ),
        migrations.AlterField(
            model_name='talababaholash',
            name='kafedra_mudiri',
            field=models.CharField(max_length=50, verbose_name='Kafedra mudiri'),
        ),
        migrations.AlterField(
            model_name='talababaholash',
            name='oraliq_nazorat_masul',
            field=models.CharField(help_text='F.I.SH', max_length=150, verbose_name='Oraliq Nazorat Masuli'),
        ),
    ]
