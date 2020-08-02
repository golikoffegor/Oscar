from .Construction import Constructions
from .Mat_trubs import Mat_trubs

#Переменные для расчета вводов стальных труб в ППУ - изоляции

diameter_PPU = 0
vvoda_PPU = 0
nopora_PPU = 0

#Переменные для расчета вводов труб типа "Изопрофлекс"

diameter_IZOP = 0
vvoda_IZOP = 0
nopora_IZOP = 0

#Переменные для расчета ж/б канала

width_mon = 0
height_mon = 0
m_mon = 0

#Переменные для расчета ж/б основания №1

width_bez_1 = 0
m_bez_1 = 0

#Переменные для расчета ж/б основания №2

width_bez_2 = 0
m_bez_2 = 0

#Перменные для расчета материалов для лотков типа Л6

l6_sht = 0
l6_l = 0
l6_dl = 0
l6_pl = 0
l6_dpl = 0

#Перменные для расчета материалов для лотков типа Л11

l11_sht = 0
l11_l = 0
l11_dl = 0
l11_pl = 0
l11_dpl = 0

#Переменные для добавления блоков ФБС

fbs336 = 0
fbs636 = 0
fbs936 = 0
fbs1236 = 0
fbs2436 = 0

#Переменная для добавления подбетонки в спецификацию

podb_B15 = 0

#Переменная для расчета силовой конструкции для стальных труб в ППУ - изоляции

sil_PPU = 0

#Переменная для расчета силовой конструкции для труб типа "Изопрофлекс"

sil_IZOP = 0



CO2_1 = Mat_trubs(diameter_PPU, vvoda_PPU, nopora_PPU, diameter_IZOP, vvoda_IZOP, nopora_IZOP, width_mon, height_mon, \
        m_mon, width_bez_1, m_bez_1, width_bez_2, m_bez_2, l6_sht, l11_sht, podb_B15, sil_PPU, sil_IZOP, l6_l, l6_dl, \
        l6_pl, l6_dpl, l11_l, l11_dl, l11_pl, l11_dpl, fbs336, fbs636, fbs936, fbs1236, fbs2436)

CO2_1.ppu()

CO2_1.izop()



CO2_2 = Constructions(diameter_PPU, vvoda_PPU, nopora_PPU, diameter_IZOP, vvoda_IZOP, nopora_IZOP, width_mon, height_mon, \
        m_mon, width_bez_1, m_bez_1, width_bez_2, m_bez_2, l6_sht, l11_sht, podb_B15, sil_PPU, sil_IZOP, l6_l, l6_dl, \
        l6_pl, l6_dpl, l11_l, l11_dl, l11_pl, l11_dpl, fbs336, fbs636, fbs936, fbs1236, fbs2436)

CO2_2.construction()