# Actividad: Reto semana 1
# Nombre: Jair Alejandro Aristizabal Albarracin
# Grupo: 17

def abstracta ( lado : int , cubos : int) -> tuple :
    # Calculos de area y volumen para un cubo individual
    area_cara=lado*lado
    area_cubo=area_cara*6
    Volumen_cubo=lado**3
    # Calculos de area y volumen de la figura completa
    area_figura=cubos*area_cubo
    volumen_figura=cubos*Volumen_cubo

    return lado , area_figura , volumen_figura

def abstracta_inv(lado: int , area_figura: int):
    # Calculos de area para un cubo individual
    area_cara=lado*lado
    area_cubo=area_cara*6

    # Calculo de la cantidad de cubos en la figura
    cubos=area_figura//area_cubo

    return cubos

#solución figura naranja - lado: 5 Cantidad de cubos:9
print("\nLa figura naranja de lado 5 y compuesta por 9 cubos tiene (lado, area, volumen) igual a: ",abstracta(5,9))
#solución Caso 1 - lado: 41 Area:90774 Volumen:620289
print(f"La figura del caso 1 (41, 90774, 620289) tiene {abstracta_inv(41,90774)} cubos.")
#solución Caso 2 - lado: 26 Area:36504 Volumen:158184
print(f"La figura del caso 2 (26, 36504, 158184) tiene {abstracta_inv(26,36504)} cubos.")
#solución Caso 3 - lado: 17 Area:15606 Volumen:44217
print(f"La figura del caso 3 (17, 15606, 44217)  tiene {abstracta_inv(17,15606)} cubos.\n")

