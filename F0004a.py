#F0004a: Bővítsük a fenti programot úgy, hogy jövőálló legyen: kérdezze meg a felhasználót, hogy melyik év van, és ezt vegye figyelembe, azaz ne mindig 2016-tal számoljon!

név = input('Hogy híjják kendet? ')
kor = input('És hány éves kend? ')
kor = int(kor)
ev = input('Mi a mostani évszám? ')
ev = int(ev)

születési_év = ev - kor
print(név, ', kend ', születési_év, '-ban született.', sep='')