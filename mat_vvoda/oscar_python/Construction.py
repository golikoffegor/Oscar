from .Mat_dicts import Materials
from rest_framework.response import Response
import json

class Constructions(Materials):
    def __init__(self, serializer):
        super().__init__(serializer)
    
    def construction(self):

        a14A3 = float()
        a12A3 = float()
        a10A3 = float()
        a6A1 = float()
        a10A1 = float()
        a8A3 = float()
        B22u5 = float()
        B7u5 = float()
        pesok = float()
        obm_bit = float()
        M100 = float()
        izol = float()
        perg = float()
        shv = float()
        mlist = float()
        polosa = float()
        gaika = int()
        shaiba = int()
        epox = float()
        bolt = int()

        def monolit():

        #Здесь материалы на 1 п.м. монолитного канала по заданным параметрам высоты и ширины
        #рассчитываемая конструкция имеет толщину стенок и днища равную 200мм

            nonlocal a14A3
            nonlocal a12A3
            nonlocal a10A3
            nonlocal a6A1
            nonlocal a10A1
            nonlocal B22u5
            nonlocal B7u5
            nonlocal pesok
            nonlocal obm_bit
            nonlocal M100
            nonlocal izol

            if self.width_mon or self.height_mon or self.m_mon != 0:
                a14A3 += (((self.width_mon + self.height_mon * 2 - 200) * 5 * 0.001) * 1.210 * 0.001) * self.m_mon * self.zap
                a12A3 += (((((self.width_mon - 60) * 5 * 0.001) + ((self.width_mon - 400) / 200 + 4)) * 0.888 * 0.001)) * self.m_mon * self.zap
                a10A3 += (((self.height_mon - 60) * 10 * 0.001) + ((self.width_mon - 400) / 200 + 4) + ((self.height_mon - 200) / 200 * 4)) *0.001 * 0.617 * self.m_mon * self.zap
                a6A1 += ((((self.height_mon - 200) / 200 * 4) / 4 / 2 * (5 / 2)) * 2 * 0.3 * 0.222) * 0.001 * self.m_mon * self.zap
                a10A1 += (((self.width_mon - 400) / 200) / 2) * (1000 / 400) * 1.01 * 0.617 * 0.001 * self.m_mon * self.zap
                B22u5 += (self.width_mon * 0.001 * 0.2 + (self.height_mon - 200) * 0.001 * 0.2 * 2) * self.m_mon * self.zap
                B7u5 += ((self.width_mon * 0.001 + 0.2) * 0.1 + 0.004) * self.m_mon * self.zap
                pesok += ((self.width_mon  * 0.001 - 0.200 * 2) * (self.height_mon * 0.001 - 0.200) + ((self.width_mon * 0.001 + 0.2) * 0.100)) * self.m_mon * self.zap
                obm_bit += (self.height_mon * 0.001 * 2 + self.width_mon * 0.001) * 0.004 * 880 * self.m_mon * self.zap
                M100 += (self.width_mon * 0.001 * 0.025 + self.width_mon * 0.001 * 0.020) * self.m_mon * self.zap
                izol += (self.width_mon * 0.001 + 0.4 * 2) * 2 * self.m_mon * self.zap

        monolit()

        def osnovanie_1():

        #Здесь материалы на 1 п.м. ж/б основания по заданным параметрам
        #рассчитываемая конструкция имеет толщину днища равную 250мм

            nonlocal pesok
            nonlocal B7u5
            nonlocal perg
            nonlocal a6A1
            nonlocal a8A3
            nonlocal a12A3

            if self.width_bez_1 or self.m_bez_1 != 0:
                pesok += (self.width_bez_1 * 0.001 * (0.250 + 0.200 + 0.150) + (self.width_bez_1 * 0.001 + 0.100 * 2) * 0.100) * self.m_bez_1 * self.zap
                B7u5 += self.width_bez_1 * 250 * 0.001 * 0.001 * self.m_bez_1 * self.zap
                perg += (self.width_bez_1 + 200) * 0.001 * 2 * self.m_bez_1 * self.zap
                a6A1 += (((self.width_bez_1 * 0.001 - 0.1)/0.4 + 0.5) * 3.66 * (250 * 0.001 - 0.06)) * 0.222 * 0.001 * self.m_bez_1 * self.zap
                a8A3 +=  (self.width_bez_1 * 0.001 - 0.05) * 7.32 * 0.395 * 0.001 * self.m_bez_1 * self.zap
                a12A3 += ((self.width_bez_1 * 0.001 - 0.1) / 0.2 + 1) * 2 * 0.888 * 0.001 * self.m_bez_1 * self.zap

        osnovanie_1()

        def osnovanie_2():

        #Здесь материалы на 1 п.м. ж/б основания по заданным параметрам
        #рассчитываемая конструкция имеет толщину днища равную 250мм

            nonlocal pesok
            nonlocal B7u5
            nonlocal perg
            nonlocal a6A1
            nonlocal a8A3
            nonlocal a12A3

            if self.width_bez_2 or self.m_bez_2 != 0:
                pesok += (self.width_bez_2 * 0.001 * (0.250 + 0.200 + 0.150) + (self.width_bez_2 * 0.001 + 0.100 * 2) * 0.100) * self.m_bez_2 * self.zap
                B7u5 += self.width_bez_2 * 250 * 0.001 * 0.001 * self.m_bez_2 * self.zap
                perg += (self.width_bez_2 + 200) * 0.001 * 2 * self.m_bez_2 * self.zap
                a6A1 += (((self.width_bez_2 * 0.001 - 0.1)/0.4 + 0.5) * 3.66 * (250 * 0.001 - 0.06)) * 0.222 * 0.001 * self.m_bez_2 * self.zap
                a8A3 +=  (self.width_bez_2 * 0.001 - 0.05) * 7.32 * 0.395 * 0.001 * self.m_bez_2 * self.zap
                a12A3 += ((self.width_bez_2 * 0.001 - 0.1) / 0.2 + 1) * 2 * 0.888 * 0.001 * self.m_bez_2 * self.zap

        osnovanie_2()

        def lotok_l6():

        #Здесь материалы на 1 метр канала по лотку Л6

            nonlocal B7u5
            nonlocal pesok
            nonlocal obm_bit
            nonlocal M100
            nonlocal izol

            if self.l6_sht != 0:
                B7u5 += (0.025 / 3) * self.l6_sht * self.zap
                pesok += (1.760 / 3) * self.l6_sht * self.zap
                obm_bit += (0.025 / 3) * 880 * self.l6_sht * self.zap
                M100 += (0.160 / 3) * self.l6_sht * self.zap
                izol += (5.280 / 3) * 2 * self.l6_sht * self.zap

        lotok_l6()

        def lotok_l11():

        #Здесь материалы на 1 метр канала по лотку Л11

            nonlocal B7u5
            nonlocal pesok
            nonlocal obm_bit
            nonlocal M100
            nonlocal izol

            if self.l11_sht != 0:
                B7u5 += (0.031 / 3) * self.l11_sht * self.zap
                pesok += (2.850 / 3) * self.l11_sht * self.zap
                obm_bit += (0.033 / 3 ) * 880 * self.l11_sht * self.zap
                M100 += (0.200 / 3) * self.l11_sht * self.zap
                izol += (6.240 / 3) * 2 * self.l11_sht * self.zap

        lotok_l11()

        def opor_PPU():

        #Здесь материалы по опорам на 1 ввод в здание для стальных труб в ППУ - изоляции

            nonlocal shv
            nonlocal mlist
            nonlocal polosa
            nonlocal gaika
            nonlocal shaiba
            nonlocal epox
            nonlocal bolt

            if self.sil_PPU != 0:
                shv += 0.058 * self.sil_PPU
                mlist += 0.039 * self.sil_PPU
                polosa += 0.013 * self.sil_PPU
                gaika += 12 * self.sil_PPU
                shaiba += 12 * self.sil_PPU
                epox += 1 * self.sil_PPU
                bolt += 12 * self.sil_PPU

        opor_PPU()

        def opor_IZOP():

        #Здесь материалы по опорам на 1 ввод в здание для труб типа "Изопрофлекс"

            nonlocal shv
            nonlocal mlist
            nonlocal polosa
            nonlocal gaika
            nonlocal shaiba
            nonlocal epox
            nonlocal bolt            
        
            if self.sil_IZOP != 0:
                shv += 0.021 * self.sil_IZOP
                mlist += 0.024 * self.sil_IZOP
                polosa += 0.013 * self.sil_IZOP
                gaika += 12 * self.sil_IZOP
                shaiba += 12 * self.sil_IZOP
                epox += 1 * self.sil_IZOP
                bolt += 12 * self.sil_IZOP

        opor_IZOP()

        def construct_name():
            if pesok or shv != 0:
                print("Строительная часть")

        construct_name()

        #Здесь функции с выводом полных названий плит, лотков и блоков ФБС

        def l6_l():
            if self.l6_l != 0:
                self.name = "l6_l"
                self.mat_name = "Лоток Л6-8/2"
                self.mat_gost = "Территориальный каталог г.Москвы"
                self.mat_izm = "шт"
                self.mat_kol = self.l6_l
                self.description()

        l6_l()

        def l6_dl():
            if self.l6_dl != 0:
                self.name = "l6_dl"
                self.mat_name = "Лоток доборный Л6д-8"
                self.mat_gost = "Территориальный каталог г.Москвы"
                self.mat_izm = "шт"
                self.mat_kol = self.l6_dl
                self.description()

        l6_dl()

        def l6_pl():
            if self.l6_pl != 0:
                self.name = "l6_pl"
                self.mat_name = "Плита перекрытия П8-8"
                self.mat_gost = "Территориальный каталог г.Москвы"
                self.mat_izm = "шт"
                self.mat_kol = self.l6_pl
                self.description()

        l6_pl()

        def l6_dpl():
            if self.l6_dpl != 0:
                self.name = "l6_dpl"
                self.mat_name = "Плита доборная П8д-8"
                self.mat_gost = "Территориальный каталог г.Москвы"
                self.mat_izm = "шт"
                self.mat_kol = self.l6_dpl
                self.description()

        l6_dpl()

        def l11_l():
            if self.l11_l != 0:
                self.name = "l11_l"
                self.mat_name = "Лоток Л11-8/2"
                self.mat_gost = "Территориальный каталог г.Москвы"
                self.mat_izm = "шт"
                self.mat_kol = self.l11_l
                self.description()

        l11_l()

        def l11_dl():
            if self.l11_dl != 0:
                self.name = "l11_dl"
                self.mat_name = "Лоток доборный Л11д-8"
                self.mat_gost = "Территориальный каталог г.Москвы"
                self.mat_izm = "шт"
                self.mat_kol = self.l11_dl
                self.description()

        l11_dl()

        def l11_pl():
            if self.l11_pl != 0:
                self.name = "l11_pl"
                self.mat_name = "Плита перекрытия П11-8"
                self.mat_gost = "Территориальный каталог г.Москвы"
                self.mat_izm = "шт"
                self.mat_kol = self.l11_pl
                self.description()

        l11_pl()

        def l11_dpl():
            if self.l11_dpl != 0:
                self.name = "l11_dpl"
                self.mat_name = "Плита доборная П11-8"
                self.mat_gost = "Территориальный каталог г.Москвы"
                self.mat_izm = "шт"
                self.mat_kol = self.l11_dpl
                self.description()

        l11_dpl()

        def fbs_3_3_6():
            if self.fbs336 != 0:
                self.name = "fbs_3_3_6"
                self.mat_name = "Фундаментный блок ФБС 3.3.6-т"
                self.mat_gost = "Территориальный каталог г.Москвы"
                self.mat_izm = "шт"
                self.mat_kol = self.fbs336
                self.description()

        fbs_3_3_6()

        def fbs_6_3_6():
            if self.fbs636 != 0:
                self.name = "fbs_6_3_6"
                self.mat_name = "Фундаментный блок ФБС 6.3.6-т"
                self.mat_gost = "Территориальный каталог г.Москвы"
                self.mat_izm = "шт"
                self.mat_kol = self.fbs636
                self.description()

        fbs_6_3_6()

        def fbs_9_3_6():
            if self.fbs936 != 0:
                self.name = "fbs_9_3_6"
                self.mat_name = "Фундаментный блок ФБС 9.3.6-т"
                self.mat_gost = "Территориальный каталог г.Москвы"
                self.mat_izm = "шт"
                self.mat_kol = self.fbs936
                self.description()

        fbs_9_3_6()

        def fbs_12_3_6():
            if self.fbs1236 != 0:
                self.name = "fbs_12_3_6"
                self.mat_name = "Фундаментный блок ФБС 12.3.6-т"
                self.mat_gost = "Территориальный каталог г.Москвы"
                self.mat_izm = "шт"
                self.mat_kol = self.fbs1236
                self.description()

        fbs_12_3_6()

        def fbs_24_3_6():
            if self.fbs2436 != 0:
                self.name = "fbs_24_3_6"
                self.mat_name = "Фундаментный блок ФБС 24.3.6-т"
                self.mat_gost = "Территориальный каталог г.Москвы"
                self.mat_izm = "шт"
                self.mat_kol = self.fbs2436
                self.description()

        fbs_24_3_6()

        #Здесь функции с выводом полных названий для каждого из материалов

        def all_a14A3():
            if a14A3 != 0:
                self.name = "all_a14A3"
                self.mat_name = "Сталь арматурная 14-А-III (А400)"
                self.mat_gost = "ГОСТ 5781-82"
                self.mat_izm = "т"
                self.mat_kol = round(a14A3 , 3)
                self.description()

        all_a14A3()

        def all_a12A3():
            if a12A3 != 0:
                self.name = "all_a12A3"
                self.mat_name = "Сталь арматурная 12-А-III (А400)"
                self.mat_gost = "ГОСТ 5781-82"
                self.mat_izm = "т"
                self.mat_kol = round(a12A3 , 3)
                self.description()

        all_a12A3()

        def all_a10A3():
            if a10A3 != 0:
                self.name = "all_a10A3"
                self.mat_name = "Сталь арматурная 10-А-III (А400)"
                self.mat_gost = "ГОСТ 5781-82"
                self.mat_izm = "т"
                self.mat_kol = round(a10A3 , 3)
                self.description()

        all_a10A3()
        
        def all_a10A1():
            if a10A1 != 0:
                self.name = "all_a10A1"
                self.mat_name = "Сталь арматурная 10-А-I (A240)"
                self.mat_gost = "ГОСТ 5781-82"
                self.mat_izm = "т"
                self.mat_kol = round(a10A1 , 3)
                self.description()

        all_a10A1()

        def all_a8A3():
            if a8A3 != 0:
                self.name = "all_a8A3"
                self.mat_name = "Сталь арматурная 8-А-III (А400)"
                self.mat_gost = "ГОСТ 5781-82"
                self.mat_izm = "т"
                self.mat_kol = round(a8A3 , 3)
                self.description()

        all_a8A3()
        
        def all_a6A1():
            if a6A1 != 0:
                self.name = "all_a6A1"
                self.mat_name = "Сталь арматурная 6-А-I (A240)"
                self.mat_gost = "ГОСТ 5781-82"
                self.mat_izm = "т"
                self.mat_kol = round(a6A1 , 3)
                self.description()

        all_a6A1()

        def all_B22u5():
            if B22u5 != 0:
                self.name = "all_B22u5"
                self.mat_name = "Смесь БСТ В22,5 П3 F100 W4" 
                self.mat_gost = None
                self.mat_izm = "м³"
                self.mat_kol = round(B22u5 , 3)
                self.description()

        all_B22u5()

        def all_B15():
            if self.podb_B15 != 0:
                self.name = "all_B15"
                self.mat_name = "Смесь БСТ B15 П4 F150 W4"
                self.mat_gost = None
                self.mat_izm = "м³"
                self.mat_kol = round(self.podb_B15 , 3)
                self.description()

        all_B15()

        def all_B7u5():
            if B7u5 != 0:
                self.name = "all_B7u5"
                self.mat_name = "Смесь БСТ B7,5 П3 F50 W2"
                self.mat_gost = None
                self.mat_izm = "м³"
                self.mat_kol = round(B7u5 , 3)
                self.description()

        all_B7u5()

        def all_pesok():
            if pesok != 0:
                self.name = "all_pesok"
                self.mat_name = "Песок строит. Мк 2,4-3,0 Г8736-93"
                self.mat_gost = None
                self.mat_izm = "м³"
                self.mat_kol = round(pesok , 3)
                self.description()

        all_pesok()

        def all_obm_bit():
            if obm_bit != 0:
                self.name = "all_obm_bit"
                self.mat_name = "Мастика битумная универсальная МБУ 16кг"  
                self.mat_gost = None
                self.mat_izm = "кг"
                self.mat_kol = round(obm_bit , 3)
                self.description()

        all_obm_bit()

        def all_M100():
            if M100 != 0:
                self.name = "all_M100"
                self.mat_name = "Раствор М100 Пк3 ПМД-5 Г28013-98"
                self.mat_gost = None
                self.mat_izm = "м³"
                self.mat_kol = round(M100 , 3)
                self.description()

        all_M100()

        def all_izol():
            if izol != 0:
                self.name = "all_izol"
                self.mat_name = "Гидростеклоизол ТКП-4,0 стеклоткань кар."
                self.mat_gost = None
                self.mat_izm = "м²"
                self.mat_kol = round(izol , 3)
                self.description()

        all_izol()

        def all_perg():
            if perg != 0:
                self.name = "all_perg"
                self.mat_name = "Пергамин П-350 Г2697-83"
                self.mat_gost = None
                self.mat_izm = "м²"
                self.mat_kol = round(perg , 3)
                self.description()

        all_perg()

        def all_shv():
            if shv != 0:
                self.name = "all_shv"
                self.mat_name = "Швеллер 16П Г8240-97 / Ст3пс" 
                self.mat_gost = None
                self.mat_izm = "т"
                self.mat_kol = round(shv , 3)
                self.description()

        all_shv()

        def all_mlist():
            if mlist != 0:
                self.name = "all_mlist"
                self.mat_name = "Лист Б-ПН-НО-10х1500х6000 /Ст3пс5"
                self.mat_gost = None
                self.mat_izm = "т"
                self.mat_kol = round(mlist , 3)
                self.description()

        all_mlist()

        def all_polosa():
            if polosa != 0:
                self.name = "all_polosa"
                self.mat_name = "Полоса 10х200-ОН-ВТ1-ВШ1-НД-ВС-ПН Ст3сп"
                self.mat_gost = "С245 ГОСТ 27772-88"
                self.mat_izm = "т"
                self.mat_kol = round(polosa , 3)
                self.description()

        all_polosa()

        def all_gaika():
            if gaika != 0:
                self.name = "all_gaika"
                self.mat_name = "Гайка М16-6H.5 (S24)"
                self.mat_gost = "ГОСТ 5927-70"
                self.mat_izm = "шт"
                self.mat_kol = gaika
                self.description()

        all_gaika()

        def all_shaiba():
            if shaiba != 0:
                self.name = "all_shaiba"
                self.mat_name = "Шайба А 16.01.08кп.016"
                self.mat_gost = "ГОСТ 11371-78"
                self.mat_izm = "шт"
                self.mat_kol = shaiba
                self.description()

        all_shaiba()

        def all_epox():
            if epox != 0:
                self.name = "all_epox"
                self.mat_name = "Эмаль эпоксидная ЭП-140 белый" 
                self.mat_gost = "ГОСТ 24709-81"
                self.mat_izm = "кг"
                self.mat_kol = round(epox , 3)
                self.description()

        all_epox()

        def all_bolt():
            if bolt != 0:
                self.name = "all_bolt"
                self.mat_name = "Самоанкерующийся болт БСР 16х150 УЗ ст.09Г2С"
                self.mat_gost = "ГОСТ 28778-90"
                self.mat_izm = "шт"
                self.mat_kol = bolt
                self.description()

        all_bolt()

        return self.spec
