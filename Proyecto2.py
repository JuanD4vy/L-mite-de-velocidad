ingr = input()
ingrs = ingr.split()
      
distanciax = float(ingrs[0]) 
vel_max = int(ingrs[1])  
tiempo = int(ingrs[2])

distancia = distanciax/1000
tiempos = tiempo/3600
velocidades = distancia/tiempos
porcentaje = vel_max + vel_max*0.20

if velocidades <= vel_max:
    print('OK')
elif distanciax and tiempo and vel_max < 0:
    print('ERROR')
elif (velocidades > vel_max) and (velocidades < porcentaje):
    print('MULTA')
elif velocidades >= porcentaje:
    print('CURSO SENSIBILIZACION')