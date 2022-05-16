chavo = int(input( ))
quico = chavo*2+4
ñoño = (chavo+quico)//5
print(chavo, quico, ñoño)

peso = ñoño
if 0 <= peso < 20:
    print('uno')
elif 21 <= peso <40:
    print('dos')
elif 41 <= peso < 80:
    print('tres')
elif peso >80:
    print('cuatro')