
from django.db import models
from django.core.validators import  MaxValueValidator,MinValueValidator


class Talaba(models.Model):
    ism = models.CharField(max_length=255)
    yosh = models.PositiveSmallIntegerField()
    Tel_raqam = models.CharField(max_length=15)
    kurs = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),MaxValueValidator(4)])

    def __str__(self):
        return self.ism
    class Meta:
        verbose_name = 'Talaba'
        verbose_name_plural = 'Talabalar'

class Muallif(models.Model):
    ism = models.CharField(max_length=255)
    t_yil = models.DateField(blank=True,null=True)
    jinsi  = models.CharField(max_length=50,choices=(('erkak', 'erkak'),('ayol',"ayol")))
    kitoblar_soni = models.PositiveSmallIntegerField(blank=True,null=True)
    tirik  = models.BooleanField(default=False)
    millat = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.ism
    class Meta:
        verbose_name = 'Muallif'
        verbose_name_plural = 'Mualliflar'

class Kitob(models.Model):
    nom = models.CharField(max_length=255)
    janr = models.CharField(max_length=50)
    sahifa = models.PositiveSmallIntegerField()
    muqova = models.CharField(
        max_length=50,
        choices=(
        ('Qattiq','Qattiq'),
        ('Yumshoq', 'Yumshoq')
    ))
    muallif = models.ManyToManyField(Muallif)
    def __str__(self):
        return self.nom

class Kutubxonachi(models.Model):
    ISH_VAQTI = (
        ('08:00-13:00','08:00-13:00'),
        ('13:00-20:00','13:00-20:00'),
        ('20:00-00:00','20:00-00:00')
    )
    ism = models.CharField(max_length=50)
    telefon_raqam = models.CharField(max_length=50)
    ish_vaqti = models.CharField(max_length=50, choices=ISH_VAQTI)
    def __str__(self):
        return self.ism
    class Meta:
        verbose_name ='Kutubxonachi'
        verbose_name_plural = ('Kutubxonachilar')

class Record(models.Model):
    talaba  = models.ForeignKey(Talaba,on_delete=models.SET_NULL,null=True)
    kitob = models.ForeignKey(Kitob,on_delete=models.SET_NULL,null=True)
    kutubxonachi = models.ForeignKey(Kutubxonachi,on_delete=models.SET_NULL,null=True)
    olingan_sana = models.DateField(auto_now_add=True,null=True)
    qaytargan_sana = models.DateField(blank=True,null=True)
    qaytardi = models.BooleanField(default=False)

    def __str__(self):
        return f" { self.talaba} {self.kitob} {self.kutubxonachi}"
    class Meta:
        verbose_name = 'Rekord'
        verbose_name_plural = "Rekordlar"
