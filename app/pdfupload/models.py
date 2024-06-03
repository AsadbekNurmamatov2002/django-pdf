from django.db import models

# Create your models here.


   
class Grops(models.Model):
    class Smester(models.TextChoices):
        BIR = "1", "1-semestr"
        IKKI = "2", "2-semestr"
        UCH = "3", "3-semestr"
        TURT = "4", "4-semestr"
        BESH = "5", "5-semestr"
        OLTI = "6", "6-semestr"
        YETTI = "7", "7-semestr"
        SAKKIZ = "8", "8-semestr"
        TUQQIZ = "9", "9-semestr"
        ON = "10", "10-semestr"
        
    class Yunalish(models.TextChoices):
        AMALIY_M_F = "AMALIY_M_F", "Amaliy matematika va fizika"
        BOSHLANGICH_T_GUMANITER_F = "2", "Boshlang\'ich ta'lim va gumaniter fanlar funkuteti"
        TABIY_FANLAR_F = "3", "Tabiy fanlar fakulteri"
        SANATSHUNOSLIK_FAKULTETE = "SANATSHUNOSLIK_FAKULTETE", "Sanatshunoslik fakul\'teti"
        JISMONIY_MADANIYAT_SPORT_VA_MK_TALIM = "JISMONIY_MADANIYAT_SPORT_VA_MK_TALIM", "Jismoniy madaniyat, sport va Maktabgacha ta'lim fakulteti"
        FILOLOGIYA_FAKULTETI = "FILOLOGIYA_FAKULTETI", "filologiya fakulteti"
    
    class Kafedra(models.TextChoices):
        TEXNOLOGIYA_T_k='TEXNOLOGIYA_T_Y', "TEXNOLOGIYA talim kafidrasi"
        RUS_TILI_ADABIYOT_K= 'RUS_TILI_ADABIYOT_K', 'Rus tili va adabiyoti kafedrasi'
        MATEMATIKA_VA_INFORMATIKA='MATEMATIKA_VA_INFORMATIKA', 'Matematika va Informatika'
        MAKTABGACHA_TALIM_K="MAKTABGACHA_TALIM_K", " Maktabgacha ta'lim kafidrasi"
        UZBEK_TILI_VA_ADABIYOTI_K='UZBEK_TILI_VA_ADABIYOTI_K', "o'zbek tili va adabiyoti kafedrasi"
        BOSHLANGICH_TALIM_K="BOSHLANGICH_TALIM_K", "Boshlang'ich talim nazariyasi kafedrasi"
        PEDAGOGIKA_K='PEDAGOGIKA_K', "Pedagogika kafedrasi"
        BOSHLANGICH_TALIM_METODIKASI_K="BOSHLANGICH_TALIM_METODIKASI_K", "Boshlang'ich talim metodikasi kafedrasi"
        PSIXOLOGIYA_K="PSIXOLOGIYA_K", 'Psixologiya kafedrasi'
        XORIJIY_TILLAR_K="XORIJIY_TILLAR_K","Xorijiy tillar kafedrasi"
        TASVIRIY_SANAT_VAmUHANDISLIK_K="TASVIRIY_SANAT_VAmUHANDISLIK_K", "Tasviriy san'at va muhandislik grafikasi kafidrasi"
        MUSIQA_TALIM_K="MUSIQA_TALIM_K", "Musiqa ta'lim kafedrasi"
        SPORT_TURLARINI_UQITISH_METO_K = 'SPORT_TURLARINI_UQITISH_METO_K', "Sport turlarini o'qitish metodikasi kafedrasi"
        KIMYO_K="KIMYO_K", "Kimyo kafedrasi"
        FIZIKA_ASTRONOMIYA_K="FIZIKA_ASTRONOMIYA_K","Fizika astronomiya kafedrasi"
        JISMONIY_MADANIYAT_NAZARIYASI_VA_MATEMATIKASI_K="JISMONIY_MADANIYAT_NAZARIYASI_VA_MATEMATIKASI_K","Jismoniy madaniyat nazariyasi va m,k"
        BIOLOGIYA_VA_GEOGRAFIYA_K="BIOLOGIYA_VA_GEOGRAFIYA_K", "Biologiya va Geografiya kafedrasi"
        IJTIMOIY_GUMANITAR_FANLAR_K="IJTIMOIY_GUMANITAR_FANLAR_K", 'Ijtimoiy gumanitar fanlar Kafedrasi'
        
    uqov_yil = models.CharField(max_length=25) 
    smester = models.CharField(max_length=8, choices=Smester.choices)
    yunalish = models.CharField(max_length=60, choices=Yunalish.choices, verbose_name="yo\'nalish")
    smester = models.CharField(max_length=60, choices=Kafedra.choices)
    fan_nomi=models.CharField(max_length=200)
    gruh_nomi=models.CharField(max_length=200)
    fan_soat =models.IntegerField()
    fan_kredit =models.CharField(max_length=25, blank=True,  help_text="F.I.SH")
    
    def __str__(self) -> str:
        return self.fan_nomi
    
    def save(self, *args, **kwargs):
        self.fan_kredit = str(int(self.fan_soat)/30)
        return super().save(*args, **kwargs)

class Talaba(models.Model):
    ism=models.CharField(max_length=250)
    familya=models.CharField(max_length=250)
    ota=models.CharField(max_length=250)
    talaba_id=models.IntegerField()
    group = models.ForeignKey(Grops, on_delete=models.CASCADE)
    def __str__(self):
        return self.familya
    
class Talababaholash(models.Model):
    grups = models.ForeignKey(Grops, on_delete=models.CASCADE)
    talaba= models.ForeignKey(Talaba, on_delete=models.CASCADE)
    ball = models.IntegerField()
    bahosi = models.IntegerField(blank=True)
    uquv_boshqarma_boshligi=models.CharField(max_length=200,  help_text="F.I.SH")
    oraliq_nazorat_masul = models.CharField(max_length=150, help_text="F.I.SH")
    kafedra_mudiri=models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.bahosi)
    
    def save(self, *args, **kwargs):
        if self.bahosi is None:
            if self.ball <=50 and self.ball>=45:
                self.bahosi = 5
            elif self.ball <45 and self.ball>=38:
                self.bahosi = 4
            elif self.ball <38 and self.ball>=30:
                self.bahosi = 3
            else:
                self.bahosi = 2
                
        return super(Talababaholash, self).save(*args, **kwargs)
    