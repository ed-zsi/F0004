#F0004d: Írj olyan programot, amelyik a felhasználótól megkérdi, hogy hány magyar mérföldre van a sárkány barlangja, és megmondja ezt kilométerben és tengeri mérföldben (mert ugye lehet, hogy hajózni is kell)!

tavolsag = int(input('Hány mérfőldre van a sárkány barlangja?'))
km = tavolsag * 8.3536
tengerimf = km/1.852
print(km,'km-re és', tengerimf, 'tengeri mérföldre van a barlang!')
