'''
SFWIT MENTORÍA TRONCO COMÚN PYTHON
ACTIVIDAD "RETO PYTHON"

INDICACIONES
Vamos a proceder a crear una lista de diccionarios, esto es:
un directorio de estudiantes de SKILLS FOR WOMEN IN TECH que participarán en una edición en línea.
Cada estudiante debe tener los siguientes atributos:

* Nombre
* Edad
* Temas
* Menores de edad

Puedes asignar los datos a mano o utilizar funciones aleatorias para llenar los campos.

ELABORÓ MARTÍNEZ URANGA MINERVA ESMERALDA
'''
keys = ['apellido','nombre','interes1','interes2','interes3','edad']
datos = [] # inicializar el arreglo a guadar los datos
parti = [] # arreglo final

#Solicitamos al usuario que ingrese los datos uno por uno

print('Datos de estudiantes dentro del programa SFWIT')
print('')


def captura(apll,nom,tem1,tem2,tem3,edad):
  
  datos = [apll, nom, tem1, tem2, tem3, edad]
  #print(datos)

  #Armamos el diccionario
  stuSFWIT = dict(zip(keys,datos)) #función nativa
  #print(stuSFWIT)

  # Agregamos un nuevo clave-valor al diccionario
  if edad <= 18:
    stuSFWIT["status"] = "menor"
  else:
    stuSFWIT["status"] = 'mayor'

  return stuSFWIT
  #print(stuSFWIT)


while True:
  print('Favor de ingresar la información en el orden solicitado')
  print('')

  apll = str(input('Apellido: '))
  nom = str(input('Nombre: '))
  tem1 = str(input('TIC favorita: '))
  tem2 = str(input('Lenguaje favorito: '))
  tem3 = str(input('Hobby: '))
  edad = int(input('Edad: '))

  parti.append(captura(apll,nom,tem1,tem2,tem3,edad))
  
  print('¿Hay más participantes por agregar?')
  print('')
  opcion = int(input('Sí: 1  /  No: 0 '))
  if opcion == 1:
    pass
  else:
    break

print('')
print('Las participantes del programa son: ')
print('')
print('Inscritas: ',parti)
print('')
print('Fin del programa')