'''
@author Camilo Martinez 
@author Camilo Figueroa
@city Bogota
@date 2022
@license gpl2
@mail
'''
import random
deportes=["FUTBOL","ATLETISMO","CICLISMO","GOLF","NATACION","TENIS","SQUASH"]
animales=["PERRO","GATO","LORO","RATON","CONEJO","PEZ","TIBURON","AGUILA"]
ciudades=["LONDRES","PARIS","MOSCU","BOGOTA","MADRID"]
x=0
n=0
v=5
listaResp=[]
lista2=[]
Seleccionlista=()
nombre=input("hola este es el juego del ahorcado, como te llamas?: ")

print("Un placer conocerte  ",nombre, " Las categorias disponibles para jugar son:  DEPORTES, ANIMALES Y CIUDADES"+"\n")
while x==0:
    while Seleccionlista != "deportes" and Seleccionlista != "animales" and Seleccionlista != "ciudades" :
        Seleccionlista=input("indica la categoria que deseas jugar:  ")
        Seleccionlista=Seleccionlista.lower()
        if Seleccionlista == "deportes":
            print("Excelente haz escogido deportes:")
            listajuego=random.choice(deportes)
            break
        elif Seleccionlista == "animales":
            print("Excelente haz escogido animale:")
            listajuego=random.choice(animales)
            break
        elif Seleccionlista == "ciudades":
            print("Excelente haz escogido ciudades:")
            listajuego=random.choice(ciudades)
            break
        else:
            print("Seleccion no valida")
    else:
        break
    listajuego=listajuego.lower()
    pista1=len(listajuego)
    print("la palabra tiene :", pista1, " letras")
        
    varExist=listajuego
    varExist=list(varExist)

    while n!=pista1 and v!=0:
        letra=input(" ingresa una letra: " )
        letra=letra.lower()
        if letra in lista2:
          print("ops, lo siento la letra ya la usaste")  
        else:
            if letra in listajuego:
               print(" adivinaste una letra, sigue asi!!!")
               lista2.append(str(letra))
               numrep=int(listajuego.count(str(letra)))
               for i in range(len(varExist)):
                   if varExist[i] == letra:
                       listaResp.append("[{}] = {}".format(i, varExist[i]))
                   
               n+=numrep
               fal=pista1-n
               print ("llevas",n,"te faltan",fal, "esa letra se repite" ,numrep, "en la palabra")
               listaResp.sort()
               print(listaResp)
            else:
                lista2.append(str(letra))
                if v!=0:
                    v-=1
                    print("Pierdes una vida, te quedan ", v)
                else:
                    print("Que triste Perdite todas las vidas")
                    print("adivinaste ", n," letras","\n",)
                    
    else:
        print("La plabra era", listajuego.upper())                    
        print("que te parecio, espero disfrutaras")
        rep=input(str("quieres volver a jugar? "))
        rep=rep.upper()
        if rep=="SI":
            x=0
            n=0
            v=5
            listaResp=[]
            lista2=[]
            Seleccionlista=()
            print(" Volvemos a Jugar")
        else:
            x=2
            print(" Gracias por jugar")
else:

        print( "Hasta Pronto")