
#--------------- Base de datos ---------------
# positivos_C19 = {
#     'Colombia ': {'Risaralda ': [( 'Pereira ', 45) , (' Dosquebradas ', 15) , ('La Virginia ', 30) ],
#                     'Quindio ': [( 'Armenia ', 75) , ('Montenegro ', 86) ]},
#     'Mexico ': {'Quintana Roo ': [( 'Benito Juarez ', 101) , (' Solidaridad ',56) ],
#                      'Nayarit ': [( 'Compostela ', 23) , ('San Blas ', 35) , ('Xalisco ', 74) , ('Del Nayar ', 46) ]}}

positivos_C19 = {
    'Colombia': {
        'Risaralda': [('Pereira', 45), ('Dosquebradas', 15), ('La Virginia', 30)],
        'Quindio': [('Armenia', 75), ('Montenegro', 86)]
    },
    'Mexico': {
        'Quintana Roo': [('Benito Juarez', 101), ('Solidaridad', 56)],
        'Nayarit': [('Compostela', 23), ('San Blas', 35), ('Xalisco', 74), ('Del Nayar', 46)]
    },
    'Other Country': {
        'State_1': [('City1_SG1', 4585), ('City2_SG1', 5824), ('City3_SG1', 4875)],
        'State_2': [('City1_SG2', 254851), ('City2_SG2', 3458)]
    }
}

# #acceder a valores por pais
# pais_key=list(positivos_C19.keys())
# print(pais_key[0])
# print(pais_key[1])
# #acceder a valores por estado
# estado_key=list(positivos_C19[pais_key[0]].keys())
# print(estado_key)
# #acceder a valores por ciudad
# ciudades_lista=positivos_C19[pais_key[0]][estado_key[0]]
# print(ciudades_lista[0][1])
# print(ciudades_lista)

# pacientes_estado=[ciudades_lista[x][1] for x in range(len(ciudades_lista))]
# print(pacientes_estado)


# #_____pacientes de todo el pais_____
# paises_lista = list(positivos_C19.keys())
# pacientes_pais=[]

# for pais in range(len(paises_lista)):
#     pacientes_estado=[]
#     estados_lista = list(positivos_C19[paises_lista[pais]].keys())
#     for estado in range(len(estados_lista)):
#         ciudades_lista = positivos_C19[paises_lista[pais]][estados_lista[estado]]
#         pacientes_estado.append([ciudades_lista[x][1] for x in range(len(ciudades_lista))])
#     pacientes_pais.append(pacientes_estado)


# #_____________Pacientes_________________
# #_____________Pacientes llave colombia_________________
# pais_key='Colombia '
# pacientes_pais=[]
# pacientes_estado=[]
# prom_paciente_estado=[]
# estados_lista = list(positivos_C19[pais_key].keys())
# for estado in range(len(estados_lista)):
#     ciudades_lista = positivos_C19[pais_key][estados_lista[estado]]
#     pacientes_estado.append([ciudades_lista[ciudad][1] for ciudad in range(len(ciudades_lista))])
#     pacientes_pais.extend([ciudades_lista[ciudad][1] for ciudad in range(len(ciudades_lista))])
# print(pacientes_estado)

# prom_paciente_estado= [sum(pacientes_estado[estado])/float(len(pacientes_estado[estado])) for estado in range(len(estados_lista))]
# print(prom_paciente_estado)

# prom_paciente_pais=sum(pacientes_pais)/float(len(pacientes_pais)) 
# print(pacientes_pais)
# print(prom_paciente_pais)
# print(max(pacientes_pais))
# print(positivos_C19[pais_key])
# maxx=86
# for estado in range(len(estados_lista)):
#     ciudades_lista = positivos_C19[pais_key][estados_lista[estado]]
#     for ciudad in ciudades_lista:
#         if ciudad[1] == maxx:
#             print(ciudad)


# #_____________Pacientes llave mexico_________________
# pais_key='Mexico '
# pacientes_estado=[]
# estados_lista = list(positivos_C19[pais_key].keys())
# for estado in range(len(estados_lista)):
#     ciudades_lista = positivos_C19[pais_key][estados_lista[estado]]
#     pacientes_estado.append([ciudades_lista[ciudad][1] for ciudad in range(len(ciudades_lista))])


#******************************************************************************************************************************
#--------------- Funcion ---------------
def analizaPacientes ( opt :int , db:dict , pais :str=''):
    
    if opt == 0:
        if pais == '':#promedio de pacientes para cada pais.
            dic_paises={}
            paises_lista = list(db.keys()) #['Colobia ', 'Mexico ']
            for paises in range(len(paises_lista)):
                pacientes_pais=[] #lista a formar con todos los valores de pacientes por pais
                estados_lista = list(db[paises_lista[paises]].keys()) #['Risaralda ', 'Quindio '] ...
                for estado in range(len(estados_lista)):
                    ciudades_lista = db[paises_lista[paises]][estados_lista[estado]] #[('Pereira ', 45), (' Dosquebradas ', 15), ('La Virginia ', 30)]...
                    pacientes_pais.extend([ciudades_lista[ciudad][1] for ciudad in range(len(ciudades_lista))])
                prom_paciente_pais=sum(pacientes_pais)/float(len(pacientes_pais))
                dic_paises.update({paises_lista[paises] : round(prom_paciente_pais,2)}) 
            return dic_paises 
        else:
            return 'La opción no recibe país'
    
    elif opt == 1:
        try:  
            dic_estados={}
            pacientes_estado=[] #lista a formar con todos los valores de pacientes por estado
            estados_lista = list(db[pais].keys()) #['Risaralda ', 'Quindio '] ...
            for estado in range(len(estados_lista)):
                ciudades_lista = db[pais][estados_lista[estado]] #[('Pereira ', 45), (' Dosquebradas ', 15), ('La Virginia ', 30)]...
                pacientes_estado.append([ciudades_lista[ciudad][1] for ciudad in range(len(ciudades_lista))])
                
            prom_paciente_estado= [sum(pacientes_estado[estado])/float(len(pacientes_estado[estado])) for estado in range(len(estados_lista))]
            for estado in range(len(estados_lista)):
                dic_estados.update({estados_lista[estado] : round(prom_paciente_estado[estado],2)}) 
            return dic_estados 
            
        except KeyError:
            return 'La opción ingresada requiere de un país valido'
    elif opt == 2:
        try:
            pacientes_estado=[] #lista a formar con todos los valores de pacientes por estado
            estados_lista = list(db[pais].keys()) #['Risaralda ', 'Quindio '] ...
            for estado in range(len(estados_lista)):
                ciudades_lista = db[pais][estados_lista[estado]] #[('Pereira ', 45), (' Dosquebradas ', 15), ('La Virginia ', 30)]...
                pacientes_estado.extend([ciudades_lista[ciudad][1] for ciudad in range(len(ciudades_lista))])
            mayor=max(pacientes_estado)
            for estado in range(len(estados_lista)):
                ciudades_lista = positivos_C19[pais][estados_lista[estado]]
                for ciudad in ciudades_lista:
                    if ciudad[1] == mayor:
                        return ciudad

        except KeyError:
            return 'La opción ingresada requiere de un país valido'
    else:
        return 'La opción no es valida'
    
print ( analizaPacientes (0, positivos_C19 , 'Mexico'))
print ( analizaPacientes (1, positivos_C19 , 'Menxico'))
print ( analizaPacientes (2, positivos_C19 ))
print ( analizaPacientes (4, positivos_C19 , 'Mexico'))
#--------------- Pruebas ---------------
print ( analizaPacientes (0, positivos_C19 ))
print ( analizaPacientes (2, positivos_C19 , 'Colombia'))
print ( analizaPacientes (1, positivos_C19 , 'Mexico'))
print ( analizaPacientes (2, positivos_C19 , 'Mexico'))
print ( analizaPacientes (5, positivos_C19 ))
