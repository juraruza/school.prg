znamky = [[3,1], [3,2], [3,1], [10,3], [4,4]]
celkova_vaha = 0
vazeny_prumer_citatel = 0
for znamka in znamky:
    celkova_vaha += znamka[0]
    vazeny_prumer_citatel += znamka[0] * znamka[1]
vazeny_prumer = vazeny_prumer_citatel / celkova_vaha
nevážený_průměr = sum(znamka[1] for znamka in znamky) /len(znamka)
rozdíl = vazeny_prumer - nevážený_průměr
print(f"celkový vážený průměr: {vazeny_prumer}")
print(f"celkový nevážený průměr: {nevážený_průměr}")
print(f"rozdíl mezi průměry: {rozdíl}")

               