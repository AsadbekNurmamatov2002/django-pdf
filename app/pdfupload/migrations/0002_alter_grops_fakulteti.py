# Generated by Django 5.0.6 on 2024-06-03 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfupload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grops',
            name='fakulteti',
            field=models.CharField(choices=[('AMALIY_M_F', 'Amaliy matematika va fizika'), ('2', "Boshlang'ich ta'lim va gumaniter fanlar funkuteti"), ('3', 'Tabiy fanlar fakulteri'), ('SANATSHUNOSLIK_FAKULTETE', "Sanatshunoslik fakul'teti"), ('JISMONIY_MADANIYAT_SPORT_VA_MK_TALIM', "Jismoniy madaniyat, sport va Maktabgacha ta'lim fakulteti"), ('FILOLOGIYA_FAKULTETI', 'filologiya fakulteti')], max_length=60, verbose_name='Fakulteti'),
        ),
    ]
