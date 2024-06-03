from django.db import models

# Create your models here.
class Fakultet(models.Model):
    name=models.CharField(max_length=200)
    dekan=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name

class Yunalish(models.Model):
    name = models.CharField(max_length=250)
    fakultet = models.ForeignKey(Fakultet, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class KafidraMudir(models.Model):
    yunalish=models.ForeignKey(Yunalish, on_delete=models.CASCADE)
    fakultet=models.ForeignKey(Fakultet, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    uqitovchi_ism = models.CharField(max_length=250, help_text='I.F.O')
    def __str__(self):
        return self.name   

class Teachers(models.Model):
    ism=models.CharField(max_length=250)
    familya=models.CharField(max_length=250)
    ota=models.CharField(max_length=250)
    
    def __str__(self):
        return self.ism
    
class Fan(models.Model):
    kafidra=models.ForeignKey(KafidraMudir, on_delete=models.CASCADE)
    fan_nome = models.CharField(max_length=200)
    fan_soat =models.IntegerField()
    fan_kredit =models.CharField(max_length=25, blank=True,  help_text="F.I.SH")
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.fan_nome
    def save(self, *args, **kwargs):
        self.fan_kredit = str(int(self.fan_soat)/30)
        return super().save(*args, **kwargs)

   
class Grops(models.Model):
    class Smester(models.TextChoices):
        BIR = "1", "1-semester"
        IKKI = "2", "2-semester"
        UCH = "3", "3-semester"
        TURT = "4", "4-semester"
        BESH = "5", "5-semester"
        OLTI = "6", "6-semester"
        YETTI = "7", "7-semester"
        SAKKIZ = "8", "8-semester"
        TUQQIZ = "9", "9-semester"
        ON = "10", "10-semester"
    uqov_yil = models.DateField() 
    smester = models.CharField(max_length=8, choices=Smester.choices, default=Smester.BIR)
    fan = models.ManyToManyField(Fan)
    name=models.CharField(max_length=200)
    yunalish = models.ForeignKey(Yunalish, on_delete=models.CASCADE)
    teachers = models.ManyToManyField(Teachers)
    
    def __str__(self) -> str:
        return self.name
    

class Talaba(models.Model):
    ism=models.CharField(max_length=250)
    familya=models.CharField(max_length=250)
    ota=models.CharField(max_length=250)
    talaba_id=models.IntegerField()
    group = models.ForeignKey(Grops, on_delete=models.CASCADE)
    yunalish = models.ForeignKey(Yunalish, on_delete=models.CASCADE)
    def __str__(self):
        return self.familya
    
class Talababaholash(models.Model):
    fan= models.ForeignKey(Fan, on_delete=models.CASCADE)
    grups = models.ForeignKey(Grops, on_delete=models.CASCADE)
    talaba= models.ForeignKey(Talaba, on_delete=models.CASCADE)
    ball = models.IntegerField()
    bahosi = models.IntegerField(blank=True)
    uquv_boshqarma_boshligi=models.CharField(max_length=200,  help_text="F.I.SH")
    or_nazorat_masul = models.CharField(max_length=150, help_text="F.I.SH")
    kafidra_m=models.ForeignKey(KafidraMudir, on_delete=models.CASCADE)
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
    