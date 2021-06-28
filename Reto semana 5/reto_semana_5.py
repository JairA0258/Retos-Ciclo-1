import json
import pandas as pd
import numpy as np


def preProcesado (DF):
    # Funcion que prepara los generos en un DF para ser codificadas en la matriz
    # Devuelve tambien los generos en una lista
    categoriasDF = DF['categories']. apply (pd. Series )
    categoriasDF ['business_id'] = DF['business_id']
    categoriasDF = categoriasDF . drop_duplicates (['business_id'])
    categoriasDF . set_index ('business_id', inplace = True )
    categories = [ categoriasDF [ categorie ]. unique () for categorie in categoriasDF.columns ]
    categories = [ categorie for lista in categories for categorie in lista if all
    ([ pd. isnull ( categorie ) == False , categorie != ' ', categorie != '', len (
    str ( categorie )) > 1])]
    categories = list ( set ( categories ))
    return categoriasDF , categories

def codificaMatriz (DF , genres : list , producto : list ):
    
    categorias_mtx = pd.DataFrame(np.zeros((len(genres), len(producto))), index = genres, columns = producto)
   
    for business in DF.index:
        for index in DF:
            categorie = DF[index][business]
            if categorie in genres: #si la categoria está en la lista de categorias
                categorias_mtx[business][categorie] = 1
    
    return categorias_mtx

def recomiendaNegocio ( url_puntuacion :str , url_perfil :str , url_recomendacion : str)->json :
  
    #----------Generar Matriz de categorias----------
    perfil_data = pd.read_json(url_perfil)

    perfil_data,lista_categorias = preProcesado(perfil_data)
    business_cat_index = perfil_data.index 
    matriz_categorias = codificaMatriz(perfil_data,lista_categorias,business_cat_index)
    
    #----------Generar Matriz de pesos y perfil de usuario----------
    puntuacion_user = pd.read_csv(url_puntuacion, sep = ';', names=['business_id', 'peso'], index_col = ['business_id'])

    for business in matriz_categorias.columns:
        if business in puntuacion_user.index:
            matriz_categorias[business] = matriz_categorias[business].apply(lambda point: float(point * puntuacion_user['peso'][business]))
    #añade la columna perfil_user con los valores sumados en cada fila
    matriz_categorias['perfil_user']=[matriz_categorias.loc[categorie, :].sum() for categorie in matriz_categorias.index]
    #a cada valor de perfil_user lo divide sobre el valor total de elementos de la matriz (total de la columa perfil_user)
    matriz_categorias['perfil_user']=matriz_categorias['perfil_user'].apply(lambda point: point / matriz_categorias['perfil_user'].sum())

    #----------Generar Matriz candidata----------
    recomendacion_data = pd.read_json(url_recomendacion)

    recomendacion_data,lista_candidata = preProcesado(recomendacion_data)
    business_can_index = recomendacion_data.index 
    matriz_candidata= codificaMatriz(recomendacion_data,lista_candidata,business_can_index)
    
    #----------Generar Matriz de candidata perfilada y ponderaciones----------
    puntuacion_user = matriz_categorias['perfil_user']
    
    #transpone la matriz para facilitar la comparacion con el insex de perfil_user
    matriz_candidata = matriz_candidata.transpose()

    #multipica cada elemento de la matriz por el perfil_user obtenido en matriz_categorias
    #si no hay perfil para la categoria, multiplica por cero
    for business in matriz_candidata.columns:
        if business in puntuacion_user.index:
            matriz_candidata[business] = matriz_candidata[business].apply(lambda point: float(point * puntuacion_user[business]))
        else:
            matriz_candidata[business] = matriz_candidata[business].apply(lambda point: float(point * 0))
    
    #regresa la matriz a su forma otiginal
    matriz_candidata = matriz_candidata.transpose()
    
    #construye el diccionario con los usuarios y las ponderaciones
    dic_ponderaciones = { user : round(matriz_candidata.loc[:,user].sum(),5) for user in matriz_candidata.columns if round(matriz_candidata.loc[:,user].sum(),5) > 0 }
    #ordena el diccionario de mayor a menor
    dic_ponderaciones = sorted(dic_ponderaciones.items(), key=lambda x: x[1], reverse=True)
    #reordena el resultado en forma de diccionario
    dic_ponderaciones = { element[0]:element[1] for element in dic_ponderaciones}
    
    return json.dumps(dic_ponderaciones, indent = 4)






#--------------- Pruebas de resultado---------------
puntuacion_url ='https://raw.githubusercontent.com/iam3mer/defioC1MTIC2022/main/reto5/C1R5-P77/pointBusiness_1.csv'
perfil_url ='https://raw.githubusercontent.com/iam3mer/defioC1MTIC2022/main/reto5/C1R5-P77/businessPerfil_1.json'
recomendacion_url ='https://raw.githubusercontent.com/iam3mer/defioC1MTIC2022/main/reto5/C1R5-P77/businessReco_1.json'

print(recomiendaNegocio ( puntuacion_url, perfil_url, recomendacion_url))

puntuacion_url ='https://raw.githubusercontent.com/iam3mer/defioC1MTIC2022/main/reto5/C1R5-P77/pointBusiness_2.csv'
perfil_url ='https://raw.githubusercontent.com/iam3mer/defioC1MTIC2022/main/reto5/C1R5-P77/businessPerfil_2.json'
recomendacion_url ='https://raw.githubusercontent.com/iam3mer/defioC1MTIC2022/main/reto5/C1R5-P77/businessReco_2.json'

print(recomiendaNegocio ( puntuacion_url, perfil_url, recomendacion_url))