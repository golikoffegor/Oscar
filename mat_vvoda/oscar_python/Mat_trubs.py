from .Mat_dicts import Materials, spusk_kran_PPU, spusk_ves_PPU, spusk_h_trub_PPU, spusk_dn_PPU, spusk_kran_IZOP, spusk_ves_IZOP, spusk_h_trub_IZOP, spusk_dn_IZOP, \
stal_dn_PPU, stal_h_PPU, stal_ves_PPU, stal_otvod_h_PPU, stal_dn_IZOP, stal_h_IZOP, stal_ves_IZOP, stal_otvod_h_IZOP, \
vozd_kran_PPU, vozd_ves_PPU, vozd_h_trub_PPU, vozd_dn_PPU, vozd_kran_IZOP, vozd_ves_IZOP, vozd_h_trub_IZOP, vozd_dn_IZOP, \
futlar_PPU, vilaterm_PPU, beton_PPU, kanat_PPU, bitum_PPU, n_opora_PPU, futlar_IZOP, beton_IZOP, m100_IZOP, vilaterm_IZOP, bitum_IZOP, n_opora_IZOP, stal_du_IZOP

class Mat_trubs(Materials):
    def __init__(self, serializer):
        super().__init__(serializer)


    def trubs(self):

        if self.diameter_PPU or self.vvoda_PPU != 0:

            def name_PPU():
                self.spec["name_PPU"] = str("Материалы и изделия на присоединения к существующим системам(в зданиях и камерах) для стальных труб в ППУ - изоляции")

            name_PPU()

            def futlars_PPU():
                for key, value in futlar_PPU.items():
                    if key == self.diameter_PPU:
                        self.name = "futlars_PPU"
                        self.mat_name = "Футляр из стальной трубы " + value + " L=700мм"
                        self.mat_gost = "Ст.20 ГОСТ 8731-74"
                        self.mat_izm = "шт"
                        self.mat_kol = self.vvoda_PPU * 2
                        self.description()

            futlars_PPU()

            def stals_PPU():
                for key, value in stal_h_PPU.items():
                    if key == self.diameter_PPU:
                        h = value
                for key, value in stal_ves_PPU.items():
                    if key == self.diameter_PPU:
                        ves = value
                for key, value in stal_dn_PPU.items():
                    if key == self.diameter_PPU:
                        self.name = "stals_PPU"
                        self.mat_name = "Труба стальная бесшовная " + value + "x" + h
                        self.mat_gost = "Ст.20 ГОСТ 8731-74"
                        self.mat_izm = "м/т"
                        kol_m = self.vvoda_PPU * 3
                        kol_ves = round(kol_m * float(ves)/1000, 3)
                        self.mat_kol = str(kol_m) + "/" + str(kol_ves)
                        self.description()

            stals_PPU()

            def spusk_trubs_PPU():
                for key, value in spusk_h_trub_PPU.items():
                    if key == self.diameter_PPU:
                        h = value
                for key, value in spusk_ves_PPU.items():
                    if key == self.diameter_PPU:
                        ves = value
                for key, value in spusk_dn_PPU.items():
                    if key == self.diameter_PPU:
                        self.name = "spusk_trubs_PPU"
                        self.mat_name = "Труба стальная бесшовная " + value + "x" + h
                        self.mat_gost = "Ст.20 ГОСТ 8731-74"
                        self.mat_izm = "м/т"
                        kol_m = self.vvoda_PPU
                        kol_ves = round(self.vvoda_PPU * float(ves) / 1000, 3)
                        self.mat_kol = str(kol_m) + "/" + str(kol_ves)
                        self.description()

            spusk_trubs_PPU()

            def vozd_trubs_PPU():
                for key, value in vozd_h_trub_PPU.items():
                    if key == self.diameter_PPU:
                        h = value
                for key, value in vozd_ves_PPU.items():
                    if key == self.diameter_PPU:
                        ves = value
                for key, value in vozd_dn_PPU.items():
                    if key == self.diameter_PPU:
                        self.name = "vozd_trubs_PPU"
                        self.mat_name = "Труба стальная бесшовная " + value + "x" + h
                        self.mat_gost = "Ст.20 ГОСТ 8731-74"
                        self.mat_izm = "м/т"
                        kol_m = self.vvoda_PPU
                        kol_ves = round(self.vvoda_PPU * float(ves) / 1000, 3)
                        self.mat_kol = str(kol_m) + "/" + str(kol_ves)
                        self.description()

            vozd_trubs_PPU()

            def otvods_PPU():
                for key, value in stal_otvod_h_PPU.items():
                    if key == self.diameter_PPU:
                        h = value
                for key, value in stal_dn_PPU.items():
                    if key == self.diameter_PPU:
                        self.name = "otvods_PPU"
                        self.mat_name = "Отвод крутоизогнутый 90 гр. " + value + "x" + h
                        self.mat_gost = "Ст.20 ГОСТ 17375-2001"
                        self.mat_izm = "шт"
                        self.mat_kol = self.vvoda_PPU*4
                        self.description()

            otvods_PPU()

            def spusk_krans_PPU():
                for key, value in spusk_kran_PPU.items():
                    if key == self.diameter_PPU:
                        self.name = "spusk_krans_PPU"
                        self.mat_name = "Шаровой кран под приварку Ру 1,6 МПа Ду" + value
                        self.mat_gost = None
                        self.mat_izm = "шт"
                        self.mat_kol = self.vvoda_PPU
                        self.description()

            spusk_krans_PPU()

            def vozd_krans_PPU():
                for key, value in vozd_kran_PPU.items():
                    if key == self.diameter_PPU:
                        self.name = "vozd_krans_PPU"
                        self.mat_name = "Шаровой кран под приварку Ру 1,6 МПа Ду" + value
                        self.mat_gost = None
                        self.mat_izm = "шт"
                        self.mat_kol = self.vvoda_PPU
                        self.description()

            vozd_krans_PPU()

            def vilaterms_PPU():
                for key, value in vilaterm_PPU.items():
                    if key == self.diameter_PPU:
                        self.name = "vilaterms_PPU"
                        self.mat_name = "Уплотнитель Вилатерм 30"
                        self.mat_gost = None
                        self.mat_izm = "пог.м"
                        self.mat_kol = round(self.vvoda_PPU * float(value), 2)
                        self.description()

            vilaterms_PPU()

            def betons_PPU():
                for key, value in beton_PPU.items():
                    if key == self.diameter_PPU:
                        self.name = "betons_PPU"
                        self.mat_name = "Смесь БСТ B15 П4 F150 W4"
                        self.mat_gost = None
                        self.mat_izm = "м3"
                        self.mat_kol = round(self.vvoda_PPU * float(value), 3)
                        self.description()

            betons_PPU()

            def kanats_PPU():
                for key, value in kanat_PPU.items():
                    if key == self.diameter_PPU:
                        self.name = "kanats_PPU"
                        self.mat_name = "Смоляной канат"
                        self.mat_gost = None
                        self.mat_izm = "пог.м"
                        self.mat_kol = round(self.vvoda_PPU * float(value), 2)
                        self.description()

            kanats_PPU()

            def bitums_PPU():
                for key, value in bitum_PPU.items():
                    if key == self.diameter_PPU:
                        self.name = "bitums_PPU"
                        self.mat_name = "Мастика битумная универсальная МБУ 16кг"
                        self.mat_gost = None
                        self.mat_izm = "кг"
                        self.mat_kol = round(self.vvoda_PPU * float(value) * 0.004 * 880, 2)
                        self.description()

            bitums_PPU()

            def izolyats_PPU():
                self.name = "izolyats_PPU"
                self.mat_name = "Изоляция трубопроводов Ду"+str(self.diameter_PPU)
                self.mat_gost = "ТС 794.01.03.00"
                self.mat_izm = "пог.м"
                self.mat_kol = self.vvoda_PPU * 3
                self.description()

            izolyats_PPU()

            def n_oporas_PPU():
                if self.nopora_PPU != 0:
                    for key, value in n_opora_PPU.items():
                        if key == self.diameter_PPU:
                            self.name = "n_oporas_PPU"
                            self.mat_name = "Опора неподвижная " + value
                            self.mat_gost = "Серия 5.903-13 вып.7-95"
                            self.mat_izm = "шт"
                            self.mat_kol = self.nopora_PPU
                            self.description()

            n_oporas_PPU()

        if self.diameter_IZOP or self.vvoda_IZOP != 0:

            def name_IZOP():
                self.spec["name_IZOP"] = str("Материалы и изделия на присоединения к существующим системам(в зданиях и камерах) для труб типа Изопрофлекс")

            name_IZOP()

            def futlars_IZOP():
                for key, value in futlar_IZOP.items():
                    if key == self.diameter_IZOP:
                        self.name = "futlars_IZOP"
                        self.mat_name = "Футляр из стальной трубы " + value + " L=700мм"
                        self.mat_gost = "Ст.20 ГОСТ 8731-74"
                        self.mat_izm = "шт"
                        self.mat_kol = self.vvoda_IZOP * 2
                        self.description()

            futlars_IZOP()

            def stals_IZOP():
                for key, value in stal_h_IZOP.items():
                    if key == self.diameter_IZOP:
                        h = value
                for key, value in stal_ves_IZOP.items():
                    if key == self.diameter_IZOP:
                        ves = value
                for key, value in stal_dn_IZOP.items():
                    if key == self.diameter_IZOP:
                        self.name = "stals_IZOP"
                        self.mat_name = "Труба Ц-" + value + "x" + h
                        self.mat_gost = "Ст.20 ГОСТ 8731-74"
                        self.mat_izm = "м/т"
                        kol_m = self.vvoda_IZOP * 3
                        kol_ves = round(kol_m * float(ves)/1000, 3)
                        self.mat_kol = str(kol_m) + "/" + str(kol_ves)
                        self.description()

            stals_IZOP()

            def spusk_trubs_IZOP():
                if self.diameter_IZOP or self.vvoda_IZOP != 0:
                    for key, value in spusk_h_trub_IZOP.items():
                        if key == self.diameter_IZOP:
                            h = value
                    for key, value in spusk_ves_IZOP.items():
                        if key == self.diameter_IZOP:
                            ves = value
                    for key, value in spusk_dn_IZOP.items():
                        if key == self.diameter_IZOP:
                            self.name = "spusk_trubs_IZOP"
                            self.mat_name = "Труба Ц-" + value + "x" + h
                            self.mat_gost = "Ст.20 ГОСТ 8731-74"
                            self.mat_izm = "м/т"
                            kol_m = self.vvoda_IZOP
                            kol_ves = round(self.vvoda_IZOP * float(ves) / 1000, 3)
                            self.mat_kol = str(kol_m) + "/" + str(kol_ves)
                            self.description()

            spusk_trubs_IZOP()

            def vozd_trubs_IZOP():
                for key, value in vozd_h_trub_IZOP.items():
                    if key == self.diameter_IZOP:
                        h = value
                for key, value in vozd_ves_IZOP.items():
                    if key == self.diameter_IZOP:
                        ves = value
                for key, value in vozd_dn_IZOP.items():
                    if key == self.diameter_IZOP:
                        self.name = "vozd_trubs_IZOP"
                        self.mat_name = "Труба Ц-" + value + "x" + h
                        self.mat_gost = "Ст.20 ГОСТ 8731-74"
                        self.mat_izm = "м/т"
                        kol_m = self.vvoda_IZOP
                        kol_ves = round(self.vvoda_IZOP * float(ves) / 1000, 3)
                        self.mat_kol= str(kol_m) + "/" + str(kol_ves)
                        self.description()

            vozd_trubs_IZOP()

            def otvods_IZOP():
                for key, value in stal_otvod_h_IZOP.items():
                    if key == self.diameter_IZOP:
                        h = value
                for key, value in stal_dn_IZOP.items():
                    if key == self.diameter_IZOP:
                        self.name = "otvods_IZOP"
                        self.mat_name = "Отвод крутоизогнутый оцинкованный 90 гр. " + value + "x" + h
                        self.mat_gost = "Ст.20 ГОСТ 17375-2001"
                        self.mat_izm = "шт"
                        self.mat_kol = self.vvoda_IZOP * 4
                        self.description()

            otvods_IZOP()

            def vozd_krans_IZOP():
                for key, value in vozd_kran_IZOP.items():
                    if key == self.diameter_IZOP:
                        self.name = "vozd_krans_IZOP"
                        self.mat_name = "Шаровой кран под приварку Ру 1,6 МПа Ду" + value
                        self.mat_gost = None
                        self.mat_izm = "шт"
                        self.mat_kol = self.vvoda_IZOP
                        self.description()

            vozd_krans_IZOP()

            def spusk_krans_IZOP():
                if self.diameter_IZOP or self.vvoda_IZOP != 0:
                    for key, value in spusk_kran_IZOP.items():
                        if key == self.diameter_IZOP:
                            self.name = "spusk_krans_IZOP"
                            self.mat_name = "Шаровой кран под приварку Ру 1,6 МПа Ду" + value
                            self.mat_gost = None
                            self.mat_izm = "шт"
                            self.mat_kol = self.vvoda_IZOP
                            self.description()

            spusk_krans_IZOP()

            def vilaterms():
                for key, value in vilaterm_IZOP.items():
                    if key == self.diameter_IZOP:
                        self.name = "vilaterms"
                        self.mat_name = "Уплотнитель Вилатерм 30"
                        self.mat_gost = None
                        self.mat_izm = "пог.м"
                        self.mat_kol = round(self.vvoda_IZOP * float(value), 2)
                        self.description()

            vilaterms()

            def betons_IZOP():
                for key, value in beton_IZOP.items():
                    if key == self.diameter_IZOP:
                        self.name = "betons_IZOP"
                        self.mat_name = "Смесь БСТ B15 П4 F150 W4"
                        self.mat_gost = None
                        self.mat_izm = "м3"
                        self.mat_kol = round(self.vvoda_IZOP * float(value), 3)
                        self.description()

            betons_IZOP()

            def m100s_IZOP():
                for key, value in m100_IZOP.items():
                    if key == self.diameter_IZOP:
                        self.name = "m100s_IZOP"
                        self.mat_name = "Раствор М100 Пк3 ПМД-5 Г28013-98"
                        self.mat_gost = None
                        self.mat_izm = "пог.м"
                        self.mat_kol = round(self.vvoda_IZOP * float(value), 2)
                        self.description()

            m100s_IZOP()

            def bitums_IZOP():
                for key, value in bitum_IZOP.items():
                    if key == self.diameter_IZOP:
                        self.name = "bitums_IZOP"
                        self.mat_name = "Мастика битумная универсальная МБУ 16кг"
                        self.mat_gost = None
                        self.mat_izm = "кг"
                        self.mat_kol = round(self.vvoda_IZOP * float(value), 2)
                        self.description()

            bitums_IZOP()

            def izolyats_IZOP():
                for key, value in stal_du_IZOP.items():
                    if key == self.diameter_IZOP:
                        self.name = "izolyats_IZOP"        
                        self.mat_name = "Изоляция трубопроводов Ду"+str(value)
                        self.mat_gost = "ТС 794.01.03.00"
                        self.mat_izm = "пог.м"
                        self.mat_kol = self.vvoda_IZOP * 3
                        self.description()

            izolyats_IZOP()

            def n_oporas_IZOP():
                for key, value in n_opora_IZOP.items():
                    if key == self.diameter_IZOP:
                        self.name = "n_oporas_IZOP"
                        self.mat_name = "Опора хомутовая "
                        self.mat_gost = "Серия 5.903-13 вып.7-95"
                        self.mat_izm = "шт"
                        self.mat_kol = self.vvoda_IZOP * 2
                        self.description()

            n_oporas_IZOP()

        return self.spec
