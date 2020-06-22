from django.db import models

class Сoefficient(models.Model):
    address = models.CharField(max_length = 128)
    name_author = models.CharField(max_length = 128)
    diameter_PPU = models.IntegerField()
    vvoda_PPU = models.IntegerField()
    nopora_PPU = models.IntegerField()
    diameter_IZOP = models.IntegerField()
    vvoda_IZOP = models.IntegerField()
    nopora_IZOP = models.IntegerField()
    width_mon = models.IntegerField()
    height_mon = models.IntegerField()
    m_mon = models.IntegerField()
    width_bez_1 = models.IntegerField()
    m_bez_1 = models.IntegerField()
    width_bez_2 = models.IntegerField()
    m_bez_2 = models.IntegerField()
    l6_sht = models.IntegerField()
    l6_l = models.IntegerField()
    l6_dl = models.IntegerField()
    l6_pl = models.IntegerField()
    l6_dpl = models.IntegerField()
    l11_sht = models.IntegerField()
    l11_l = models.IntegerField()
    l11_dl = models.IntegerField()
    l11_pl = models.IntegerField()
    l11_dpl = models.IntegerField()
    fbs336 = models.IntegerField()
    fbs636 = models.IntegerField()
    fbs936 = models.IntegerField()
    fbs1236 = models.IntegerField()
    fbs2436 = models.IntegerField()
    podb_B15 = models.IntegerField()
    sil_PPU = models.IntegerField()
    sil_IZOP = models.IntegerField()

    def __str__(self):
        return "Данные по адресу: %s" % (self.address)

    class Meta:
        verbose_name = "Коэффициенты"
        verbose_name_plural = "Коэффициенты"