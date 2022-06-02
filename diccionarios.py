db={}
cont=len(db)
print(cont)
nom=input("ingrese sus nombres: ")
ape=input("ingrese sus apellidos: ")
edad=input("ingrese su edad: ")
id=input("ingrese su id: ")

def creacionUser(nom,ape,edad,id):
  user=dict(nombre=nom, apellido=ape, edad=edad, id=id)
  return user
def almacenarEnDb():
    db.update({cont:creacionUser(nom,ape,edad,id)})
    return db
def addUser(cont):
    print(cont)
    res=input("quiere agregar otro usuario")
    cont+=1
    while res=="si":
        nom=input("ingrese sus nombres: ")
        ape=input("ingrese sus apellidos: ")
        edad=input("ingrese su edad: ")
        id=input("ingrese su id: ")
        user=dict(nombre=nom, apellido=ape, edad=edad, id=id)
        db.update({cont:user})
        res=input("quiere agregar otro usuario")

creacionUser(nom,ape,edad,id)
almacenarEnDb()
addUser(cont)
print(cont)
print(db)





"""def modificarUser1(user1):
  res3=input("Que dato deseas cambiar: ")
  if res3=="nombre":
    nomnuevo=input("Ingrese su nombre: ")
    user1.update({"Nombre":nomnuevo})
  elif res3=="apellido":
    apenuevo=input("Ingrese su Apellido: ")
    user1.update({"Apellido":apenuevo})
  elif res3=="edad":
    edadnuevo=input("Ingrese su Edad: ")
    user1.update({"Edad":edadnuevo})
  elif res3=="id":
    idnuevo=input("Ingrese su Id: ")
    user1.update({"Id":idnuevo})
  print("------------------------------------")
  print("Sus datos fueron actualizados")
  print("------------------------------------")
  print(user1)
  print("------------------------------------")
  return (user1)

def listarDatos(user1):
  res=input("Quieres ver los datos ingresados?")
  if res=="si":
    print(user1)

creacionUser1(user1)
print("------------------------------------")
print("El usuario creado fue: ")
print("------------------------------------")
print(user1)
print("------------------------------------")
res2=input("Todos los datos estan correctos?: ")
while res2=="no":
  modificarUser1(user1)
  res2=input("Todos los datos estan correctos?: ")
print("------------------------------------")
DB.update({"user1":user1})
print("Usuario registrado con exito en la base de datos")
print("------------------------------------")
listarDatos(DB)"""