# Actividad: Reto semana 4
# Nombre: Jair Alejandro Aristizabal Albarracin
# Grupo: 17

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
    },'COUNTRY': {
        'State_4': [('City_1', 234), ('City_2', 434), ('City_3', 987)],
        'State_5': [('City_a', 123), ('City_b', 5454)]
    },
}

#--------------- Funcion ---------------
def analizaPacientes ( opt :int , db:dict , pais :str=''):

    if opt<0 or opt>2:
        return 'La opción no es valida'
    else:
        #----------Listas comunes para todas las opciones----------
        lista_paises = list(db.keys()) 
        #['Colombia ', 'Mexico ']
        lista_estados = [list(db[lista_paises[pais_idx]].keys()) for pais_idx in range(len(lista_paises))] 
        # [['Risaralda ', 'Quindio '], ['Quintana Roo ', 'Nayarit ']]
        lista_ciudades = [[db[lista_paises[pais_idx]][lista_estados[pais_idx][estado_idx]] for estado_idx in range(len(lista_estados[pais_idx]))] for pais_idx in range(len(lista_paises))]
        # [[[('Pereira ', 45), (' Dosquebradas ', 15), ('La Virginia ', 30)], [('Armenia ', 75), ('Montenegro ', 86)]], [[('Benito Juarez ', 101), (' Solidaridad ', 56)], [('Compostela ', 23), ('San Blas ', 35), ('Xalisco ', 74), ('Del Nayar ', 46)]]]
        
        if opt == 0:
            if pais == '':#promedio de pacientes para cada pais.
                total_pacientes_pais = [ [lista_ciudades[pais_idx][estado_idx][ciudad_idx][1] for estado_idx in range(len(lista_estados[pais_idx])) for ciudad_idx in range(len(lista_ciudades[pais_idx][estado_idx]))] for pais_idx in range(len(lista_paises)) ]
                # promedio_pacientes_pais = [reduce(lambda a,b: a + b, total_pacientes_pais[pais_idx])/len(total_pacientes_pais[pais_idx]) for pais_idx in range(len(total_pacientes_pais))]
                promedio_pacientes_pais = [sum(total_pacientes_pais[pais_idx])/len(total_pacientes_pais[pais_idx]) for pais_idx in range(len(total_pacientes_pais))]
                dic_pacietes_pais = {lista_paises[pais_idx]:round(promedio_pacientes_pais[pais_idx],2) for pais_idx in range(len(lista_paises))}
                return dic_pacietes_pais
            else:
                return 'La opción no recibe país'

        try: #evalua si se ha ingresado una key incorrecta o si no se ha ingresado
            pais_idx = lista_paises.index(pais)
            total_pacientes_estado = [[lista_ciudades[pais_idx][estado_idx][ciudad_idx][1] for ciudad_idx in range(len(lista_ciudades[pais_idx][estado_idx]))] for estado_idx in range(len(lista_estados[pais_idx]))]
                
            if opt == 1: #porcentaje de pacientes por estado
                promedio_pacientes_estado = [sum(total_pacientes_estado[estado_idx])/len(total_pacientes_estado[estado_idx]) for estado_idx in range(len(total_pacientes_estado))]
                dic_pacietes_estado = {lista_estados[pais_idx][estado_idx]:round(promedio_pacientes_estado[estado_idx],2) for estado_idx in range(len(lista_estados[pais_idx]))}
                return dic_pacietes_estado

            elif opt == 2: #mayor numero de pacientes en una ciudad 
                total_pacientes = [total_pacientes_estado[estado_idx][ciudad_idx] for estado_idx in range(len(total_pacientes_estado)) for ciudad_idx in range(len(total_pacientes_estado[estado_idx])) ]
                pacientes_maximo = max(total_pacientes)
                
                for estado_idx in range(len(lista_ciudades[pais_idx])):
                    for ciudad_idx in range(len(lista_ciudades[pais_idx][estado_idx])):
                        if lista_ciudades[pais_idx][estado_idx][ciudad_idx][1] == pacientes_maximo:
                            return lista_ciudades[pais_idx][estado_idx][ciudad_idx]
        except KeyError:
            return 'La opción ingresada requiere de un país valido'
        except ValueError:
            return 'La opción ingresada requiere de un país valido'

#--------------- Pruebas de errores---------------
print("Pruebas de errores")
print("\n***ingresar pais en opcion 0***\n")
print ( analizaPacientes (0, positivos_C19 , 'Mexico'))
print("\n***ingresar mal o no ingresar pais en opcion 1***\n")
print ( analizaPacientes (1, positivos_C19 , 'Menxico'))
print ( analizaPacientes (1, positivos_C19 , 1))
print ( analizaPacientes (1, positivos_C19 ))
print("\n***ingresar mal o no ingresar pais en opcion 2***\n")
print ( analizaPacientes (2, positivos_C19 , 'Colombina'))
print ( analizaPacientes (2, positivos_C19 , 1))
print ( analizaPacientes (2, positivos_C19 ))
print("\n***ingresarun valor diferente de 0,1,2***\n")
print ( analizaPacientes (4, positivos_C19 , 'Mexico'))
print ( analizaPacientes (-1, positivos_C19 , 'Colombia'))
print ()

#--------------- Pruebas para cada ciudad---------------
print("Pruebas para cada ciudad\n")
print("opcion 0:")
print ( analizaPacientes (0, positivos_C19 ))
print("opcion 1:")
print ( analizaPacientes (1, positivos_C19 , 'Colombia'))
print ( analizaPacientes (1, positivos_C19 , 'Mexico'))
print ( analizaPacientes (1, positivos_C19 , 'Other Country'))
print ( analizaPacientes (1, positivos_C19 , 'COUNTRY'))
print("opcion 2:")
print ( analizaPacientes (2, positivos_C19 , 'Colombia'))
print ( analizaPacientes (2, positivos_C19 , 'Mexico'))
print ( analizaPacientes (2, positivos_C19 , 'Other Country'))
print ( analizaPacientes (2, positivos_C19 , 'COUNTRY'))
print ()

#--------------- Pruebas de resultado---------------
print("Pruebas de resultado guias\n")
print ( analizaPacientes (0, positivos_C19 ))
print ( analizaPacientes (2, positivos_C19 , 'Colombia'))
print ( analizaPacientes (1, positivos_C19 , 'Mexico'))
print ( analizaPacientes (2, positivos_C19 , 'Mexico'))
print ( analizaPacientes (5, positivos_C19 ))
print ()
