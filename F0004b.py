#F0004b: A születési_év ismeretében írjuk ki, hogy várhatóan melyik évben érettségizik (érettségizett) a felhasználó. Az egyszerűség végett feltételezzük, hogy mindenki 18 évesen érettségizik. (Khmm..)

név = input('Hogy híjják kendet? ')
kor = input('És hány éves kend? ')
kor = int(kor)
ev = input('Mi a mostani évszám? ')
ev = int(ev)

születési_év = ev - kor
erettsegi = születési_év + 18

print(név, ', kend ', születési_év, '-ban született.', sep='')
print(erettsegi,'ben/ban tette le vagy fogja letenni kend az érettségit!!', sep='-')