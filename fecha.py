''' 
SFWIT MENTORÍA TRONCO COMÚN PYTHON
ACTIVIDAD "RETO PYTHON"

INDICACIONES
Función ValidarFecha: Recibe un día, mes y año correspondiente a una fecha y devuelve si la fecha es correcta o no.
Si introducimos un mes incorrecto, la función DiasDelMes devuelve 0 por lo tanto la fecha va a ser incorrecta.
(Parámetros de entrada: día, mes y año)
Dato devuelto: Valor lógico indicando si es correcta (Verdadero) o no (Falso)

ELABORÓ: MARTÍNEZ URANGA MINERVA ESMERALDA
'''
print("Validación de fechas de los últimos 125 años")
print('')

c = True
f = False

def restmes(m,d):
  metreu = [1,3,5,7,8,10,12] # mes con 31 días
  mtre = [4,6,9,11] #mes con 30 días

  if m in mtre and d <= 30:
    return c
  elif m in metreu and d <=31:
    return c
  else:
    return f

def febBis(y,d):
  yb =1900 #inicio
  listab = [] #arreglo años bisiestos
  b = 'Año Bisiesto'
  n = 'Año normal'
  
  while yb <= 2025:
    yb = yb + 4
    listab.append(yb) #guardo la lista
    
  #print(listab)

  if y in listab and d <= 29:
    return c,b
    #print('febrero bisiesto')
  elif d <=28:
    return c, n
    #print('febrero no bisiesto')
  else:
    return f
    #print('No válido para febrero')
  
#datep1 = febBis(y,m,d)
#print(datep1)

def datevalid(d,m,y):
  if (d >= 1 and d <= 31) and (m >= 1 and m <= 12) and (y >= 1900 and y <= 2025):
    if m == 2:
      datep1 = febBis(y,d)
      return datep1
    elif m != 2:
      datep1 = restmes(m,d)
      return datep1
  else:
    return f

while True:
  d = int(input('Ingresa el día: ')) 
  m = int(input('Ingresa el mes: '))
  y = int(input('Ingresa el año: '))
  
  datep2 = datevalid(d,m,y)
  print('Date: ',datep2)

  print('')
  print('¿Desea intentar con otra fecha?')
  print('')
  opcion = int(input('Si = 1 / No = 0 '))
  if opcion == 1:
    pass
  else:
    break

print('')
print('Fin del programa')
