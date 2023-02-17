import random

cont = "Si"
intent_final = int(0)
partidas_ganadas = 0
perc_final = 0
intento_anterior = 0
intento_mayor = 0


while cont == "Si" or cont == "si":
   número = random.randint(1, 100)
   intentosRealizados = int(0)
   Num_max=100
   Num_min=1
   intent=0
   intent = int(input("Cuants intents vols realitzar:"))   
   while intentosRealizados < intent:
      print('Intenta adivinar.')
      estimación = input()
      estimación = int(estimación)

      intentosRealizados = intentosRealizados + 1

      if estimación < número:
         Num_min=estimación
         print('Tu estimación es muy baja. El numero esta entre ' , Num_min , ' y ' , Num_max)

      if estimación > número:
         Num_max=estimación
         print('Tu estimación es muy alta.El numero esta entre ' , Num_min , ' y ' , Num_max)

      if estimación == número:
         break

   if estimación == número:
      print('¡Buen trabajo! ¡Has adivinado mi número en ' ,intentosRealizados, ' intentos!')
      intent_final += intentosRealizados
      if intentosRealizados < intento_anterior:
         intento_menor = intentosRealizados
      elif intentosRealizados > intento_anterior:
         intento_mayor = intentosRealizados
      intento_anterior = intentosRealizados
      partidas_ganadas = partidas_ganadas + 1
      cont = input("Si vols continuar escriu: si/ Si no vols escriu qualsevol altra cosa")

   if estimación != número:
      número = str(número)
      print('Nada!. El número que estaba pensando era ' + número)
      cont = input("Si vols continuar escriu: si/ Si no vols escriu qualsevol altra cosa")

perc_final = intent_final / partidas_ganadas
print("La media de intentos es: " ,perc_final)
print("El intento mayor es: " ,intento_mayor)
print("El intento menor es: " ,intento_menor)