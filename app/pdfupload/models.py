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
        
    class Fakultet(models.TextChoices):
        AMALIY_M_F = "AMALIY_M_F", "Amaliy matematika va fizika"
        BOSHLANGICH_T_GUMANITER_F = "2", "Boshlang\'ich ta'lim va gumaniter fanlar funkuteti"
        TABIY_FANLAR_F = "3", "Tabiy fanlar fakulteri"
        SANATSHUNOSLIK_FAKULTETE = "SANATSHUNOSLIK_FAKULTETE", "Sanatshunoslik fakul\'teti"
        JISMONIY_MADANIYAT_SPORT_VA_MK_TALIM = "JISMONIY_MADANIYAT_SPORT_VA_MK_TALIM", "Jismoniy madaniyat, sport va Maktabgacha ta'lim fakulteti"
        FILOLOGIYA_FAKULTETI = "FILOLOGIYA_FAKULTETI", "filologiya fakulteti"
    
    class Yunalish(models.TextChoices):
        # matematika va fizika
        M_VA_I_Y="M_VA_I_Y", "Matematika va informatika"
        F_VA_A_Y="F_VA_A_Y", "Fizika va astronomiya"
        # Boshlang'ich talim
        BOSH_TALIM_Y="BOSH_TALIM_Y", "Boshlang'ich ta'lim"
        TARIX_Y="TARIX_Y",  "Tarix "
        # Tabiy fanlar
        BIOLOGIYA ="BIOLOGIYA", 'Biologiya'
        GEOGRAFIYA_VA_IQTISODIY_B_y="GEOGRAFIYA_VA_IQTISODIY_B_y", "Geografiya va iqtisodiy bilim asoslari"
        KIMYO="KIMYO", 'Kimyo'
        
        # Sanatshinoslik Fakultiti
        MUSIQA_TA_Y="MUSIQA_TA_Y", "Musiqa ta'limi"
        TASVIR_S_Y="TASVIR_S_Y", "Tasviriy san'at muxandislik grafikasi"
        TEXNOLOGIK_T_F_K="TEXNOLOGIK_T_F_K", "Texnologik ta'lim Fakultet kvalifikatsiyasi"
        # Sport 
        JISMONIY_MAD="JISMONIY_MAD","Jismoniy madaniyat"
        SPORT_FAOLIYATI="SPORT_FAOLIYATI", "Sport faoliyati"
        MAKTABGACHA_TALIM="MAKTABGACHA_TALIM", "Maktabgacha ta'lim"
        # filogiya fakultet
        UZBEK_T_ADABIYOT="UZBEK_T_ADABIYOT", "O'zbek tili va adabiyoti"
        UZGA_TILLI_GRUHLARGA_RUS_T="UZGA_TILLI_GRUHLARGA_RUS_T", "O'zbek tilli guruhlarga rus tili"
        XORIJIY_TIL_ADABIYOTI_ING="XORIJIY_TIL_ADABIYOTI_ING","Xorijiy til va adabiyoti: ingliz tili"
                
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
        
    uquv_yil = models.CharField(max_length=25, verbose_name="o'quv yili") 
    smester = models.CharField(max_length=8, choices=Smester.choices, verbose_name="Semestr")
    yunalish=models.CharField(max_length=80, choices=Yunalish.choices, verbose_name="Yo'nalish")
    fakulteti = models.CharField(max_length=60, choices=Fakultet.choices, verbose_name="Fakulteti")
    kafedra = models.CharField(max_length=60, choices=Kafedra.choices, verbose_name="Kafedra")
    fan_nomi=models.CharField(max_length=200, verbose_name="Fan nomi")
    gruh_nomi=models.CharField(max_length=200, verbose_name="Guruh nomi")
    fan_soat =models.IntegerField()
    fan_kredit =models.CharField(max_length=25, blank=True, verbose_name="Fan krediti")
    
    def __str__(self) -> str:
        return self.gruh_nomi
    
    def save(self, *args, **kwargs):
        self.fan_kredit = str(int(self.fan_soat)/30)
        return super().save(*args, **kwargs)

class Talaba(models.Model):
    ism=models.CharField(max_length=250, verbose_name='Ismi')
    familya=models.CharField(max_length=250, verbose_name="Familyasi")
    ota=models.CharField(max_length=250, verbose_name="Otasining ismi")
    talaba_id=models.IntegerField(verbose_name="Talaba ID")
    gruh = models.ForeignKey(Grops, on_delete=models.CASCADE, verbose_name="Gruh")
    def __str__(self):
        return self.familya
    
class Talababaholash(models.Model):
    gruh = models.ForeignKey(Grops, on_delete=models.CASCADE, verbose_name="Gruh")
    talaba= models.ForeignKey(Talaba, on_delete=models.CASCADE, verbose_name="Talabalar")
    ball = models.IntegerField()
    bahosi = models.IntegerField(blank=True)
    uquv_boshqarma_boshligi=models.CharField(max_length=200, verbose_name="O'quv boshqarma boshlig'i", help_text="F.I.SH")
    oraliq_nazorat_masul = models.CharField(max_length=150, help_text="F.I.SH", verbose_name="Oraliq Nazorat Masuli")
    kafedra_mudiri=models.CharField(max_length=50, verbose_name="Kafedra mudiri")
    
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
    