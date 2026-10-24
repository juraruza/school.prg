class Graph:
    def __init__(self, orientovany=False):
        self.orientovany = orientovany
        self.vrcholy = []
        self.hrany = []

    def pridej_vrchol(self, uzel):
        if uzel not in self.vrcholy:
            self.vrcholy.append(uzel)

    def odeber_vrchol(self, uzel):
        if uzel in self.vrcholy:
            self.vrcholy.remove(uzel)
            nove_hrany = []
            for u, v, w in self.hrany:
                if u != uzel and v != uzel:
                    nove_hrany.append((u, v, w))
            self.hrany = nove_hrany

    def pridej_hranu(self, odkud, kam, vaha=None):
        self.pridej_vrchol(odkud)
        self.pridej_vrchol(kam)
        self.hrany.append((odkud, kam, vaha))

    def odeber_hranu(self, odkud, kam):
        for h in self.hrany:
            if h[0] == odkud and h[1] == kam:
                self.hrany.remove(h)
                break

    def analyze(self):
        v = len(self.vrcholy)
        e = len(self.hrany)

       
        typ_grafu = "orientovany graf" if self.orientovany else "neorientovany graf"

       
        ma_vahy = False
        for _, _, w in self.hrany:
            if w is not None:
                ma_vahy = True
                break
        ohodnoceni = "graf je ohodnoceny ma vahy u hran" if ma_vahy else "graf neni ohodnoceny hrany nemaji vahy"

       
        ma_smycku = False
        smyckove_uzly = []
        for u, k, _ in self.hrany:
            if u == k:
                ma_smycku = True
                if u not in smyckove_uzly:
                    smyckove_uzly.append(u)
        if ma_smycku:
            smycky_info = f"graf ma smycky v uzlech {smyckove_uzly}"
        else:
            smycky_info = "graf nema zadne smycky"

       
        navstivene = []
        if v > 0:
            fronta = [self.vrcholy[0]]
            navstivene.append(self.vrcholy[0])
            while len(fronta) > 0:
                aktualni = fronta.pop(0)
                sousede = []
                for odkud, kam, _ in self.hrany:
                    if odkud == aktualni and kam not in sousede:
                        sousede.append(kam)
                    if not self.orientovany and kam == aktualni and odkud not in sousede:
                        sousede.append(odkud)
                for s in sousede:
                    if s not in navstivene:
                        navstivene.append(s)
                        fronta.append(s)

        if v == 0:
            souvislost = "graf je prazdny"
        elif len(navstivene) == v:
            souvislost = "graf je souvisly vsechno je propojene"
        else:
            souvislost = "graf neni souvisly nektere casti jsou oddelene"

        
        if v <= 4:
            planarni = "je planarni da se nakreslit na papir aniz by se krizily cary"
        elif e > (3 * v - 6):
            planarni = "neni planarni ma moc car takze se musi krizit"
        else:
            planarni = "pravdepodobne je planarni pocet car splnuje podminku"

       
        if ma_smycku:
            chrom_cislo = "nelze obarvit protoze uzel se smyckou sousedi sam se sebou"
        elif v == 0:
            chrom_cislo = "0 barev"
        elif e == 0:
            chrom_cislo = "1 barva staci protoze tu nejsou zadne cary"
        else:
            barvy = {}
            for uzel in self.vrcholy:
                zakazane = []
                for odkud, kam, _ in self.hrany:
                    if odkud == uzel and kam in barvy:
                        zakazane.append(barvy[kam])
                    if kam == uzel and odkud in barvy:
                        zakazane.append(barvy[odkud])
                barva = 1
                while barva in zakazane:
                    barva += 1
                barvy[uzel] = barva
            chrom_cislo = f"{max(barvy.values())} barvy"

       
        stupne = {}
        for uzel in self.vrcholy:
            pocet = 0
            for odkud, kam, _ in self.hrany:
                if odkud == uzel:
                    pocet += 1
                if not self.orientovany and kam == uzel and odkud != uzel:
                    pocet += 1
            stupne[uzel] = pocet

     
        print("VYSLEDKY KOMPLETNI ANALYZY GRAFU")
        print("Typ grafu:", typ_grafu)
        print("Pocet vrcholu:", v)
        print("Seznam vrcholu:", self.vrcholy)
        print("Pocet hran:", e)
        print("Seznam hran:", self.hrany)
        print("Ohodnoceni:", ohodnoceni)
        print("Smycky:", smycky_info)
        print("Souvislost:", souvislost)
        print("Planarita:", planarni)
        print("Chromaticke cislo:", chrom_cislo)
        print("Pocet sousedu pro kazdy vrchol:", stupne)