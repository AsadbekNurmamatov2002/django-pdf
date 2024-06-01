from django.db import models

# Create your models here.
class Fakultet(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name
    
class Yunalish(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name
    


class Teachers(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
    
class Fan(models.Model):
    fan_nome = models.CharField(max_length=200)
    fan_soat =models.IntegerField()
    fan_kredit =models.CharField(blank=True)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.fan_nome
    def save(self, *args, **kwargs):
        self.fan_kredit = str(int(self.fan_soat)/30)
        return super().save(*args, **kwargs)
     
class Grops(models.Model):
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    yunalish = models.ForeignKey(Yunalish, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name
    

 
class Talaba(models.Model):
    class Smester(models.TextChoices):
        BIR = "BIR", "1-semester"
        IKKI = "IKKI", "2-semester"
        UCH = "UCH", "3-semester"
        TURT = "TURT", "4-semester"
        BESH = "BESH", "5-semester"
        OLTI = "OLTI", "6-semester"
        YETTI = "YETTI", "7-semester"
        SAKKIZ = "SAKKIZ", "8-semester"
        TUQQIZ = "TUQQIZ", "9-semester"
        ON = "ON", "10-semester"
    group = models.ForeignKey(Grops, on_delete=models.CASCADE)
    smester = models.CharField(max_length=8, choices=Smester.choices, default=Smester.BIR)
    fio=models.CharField(max_length=350)
    talaba_id=models.IntegerField()
    

class Baholash(models.Model):
    fakultet = models.ForeignKey(Fakultet, on_delete=models.CASCADE)
    grops = models.ForeignKey(Grops, on_delete=models.CASCADE)
    ball = models.IntegerField()
    bahosi = models.IntegerField()
    
    def __str__(self):
        return str(self.bahosi)
    
    # def clean(self) -> None:
    #     if self.ball
    #     return super().clean()