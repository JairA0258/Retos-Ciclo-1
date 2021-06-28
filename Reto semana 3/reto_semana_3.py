# Actividad: Reto semana 3
# Nombre: Jair Alejandro Aristizabal Albarracin
# Grupo: 17

from math import ceil

def bancoAmigo ( nuip : int , depositos : list) -> tuple : 
    # Parametros
    # nuip ( int ): Numero de identificacion del usuario
    # list ([]) : lista con los 12 depositos del mes Retorno
    # Tuple : de la forma ( ahorroTotal , interesGenerado , montoFinal)
    
    ahorroTotal=0
    interesMes=0
    interesAnual=0
    totalMesAnterior=0
    interesGenerado=0
    montoFinal=0
    rendimiento=0
    
    for mes in range(len(depositos)):

#-------calculo ahorro total
        ahorroTotal += depositos[mes]

#-------calculo interes 
        A = totalMesAnterior + depositos[mes] 
        if depositos[mes] >= 300000:
            interesMes = A * 0.05
        else:
            interesMes = 0

        interesAnual += interesMes 
        totalMesAnterior = A + interesMes
        
        # print(f"Ahorro mes {mes+1} ->")
        # print(f"Deposito: {depositos[mes]}")
        # print(f"A: {A}")
        # print(f"Interes: {interesMes}")
        # print(f"Total: {totalMesAnterior}")
        # print("-"*20)
        
#---calculo del rendimiento adicional
    if ahorroTotal > 3600000:
        rendimiento = ahorroTotal * 0.12
    else:
        rendimiento = ahorroTotal * 0.07

#---calculo de interes generado
    interesGenerado = interesAnual + rendimiento

#---calculo de monto final
    montoFinal= ahorroTotal + interesGenerado
    
    # print(f"Interes Anual: {interesAnual}")
    # print(f"Rendimiento: {rendimiento}")
    # print(f"Interes Generado: {interesGenerado}")
    # print(f"Monto final: {montoFinal}")

    return nuip , ahorroTotal , ceil ( interesGenerado ), ceil (
    montoFinal )


#---------- Pruebas ----------
# Caso de prueba 1:
print ( f"obtenido -> {bancoAmigo (2148542 , [300000 ,450000 ,0 ,0 ,0 ,0 ,260000 ,0 ,500000 ,0 ,420000 ,0])}")
print("esperado -> (2148542, 1930000, 369584, 2299584)")
# Caso de prueba 2:
print ( f"obtenido -> {bancoAmigo (10821247 , [50000 ,0 ,350000 ,0 ,720000 ,0 ,220000 ,0 ,0 ,455000 ,0 ,60000])}")
print("esperado -> (10821247, 1855000, 300450, 2155450)")
# Caso de prueba 3:
print ( f"obtenido -> {bancoAmigo (1254221 , [0 ,0 ,700000 ,1520000 ,0 ,0 ,0 ,580000 ,0 ,520000 ,0 ,0])}")
print("esperado -> (1254221, 3320000, 708295, 4028295)")

