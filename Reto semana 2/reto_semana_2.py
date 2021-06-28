# Actividad: Reto semana 2
# Nombre: Jair Alejandro Aristizabal Albarracin
# Grupo: 17

def facturas ( opcion : int , idCliente : int = 0, numFactura : int = 0, valor : int = 0, db: dict = {}) -> dict :
    if opcion == 0: # Crear nuevo usuario
        
        if numFactura == 0 and valor == 0:
            #se crea el usuario e imprime
            db[idCliente]= {} 
            factura_msj = {str(idCliente):'Cliente creado'} 
        else:
            # Error, el usuario no se puede crear
            factura_msj = {str(idCliente):'No existe el cliente'}

    elif opcion == 1: #Añadir factura
        
        if idCliente in db:
            #el usuario existe y se crea la factura
            db[idCliente].update({numFactura: valor})
            factura_msj = {'cliente': idCliente, 'factura': numFactura, 'abono': 0, 'valor': valor}
        else:
            # Error, no existe el usuario
            factura_msj = {str(idCliente):'No existe el cliente'}

    elif opcion == 2: #Abono o Pago total de factura
       
        if idCliente in db:
            #el usuario existe y se realiza el abono. 
            valor_restante = db[idCliente][numFactura] - valor
            factura_msj = {'cliente': idCliente, 'factura': numFactura, 'abono': valor, 'valor': valor_restante}

            #si se finaliza el pago, la factura se elimina
            if valor_restante > 0:
                #realiza el abono
                db[idCliente][numFactura] = valor_restante
            else:
                #la factura se elimina
                db[idCliente].pop(numFactura)
        else:
            # Error, no existe el usuario
            factura_msj = {str(idCliente):'No existe el cliente'}

    elif opcion == 3: #Mostrar BD
       
        factura_msj = {'print':'estado de la base de datos'}
    
    return factura_msj, db


msj , dbFacturas = facturas (0,2541)
print (msj , dbFacturas)
msj , dbFacturas = facturas (1,2541,1,300000,db = dbFacturas)
print (msj , dbFacturas)
msj , dbFacturas = facturas (2,2541,1,25000.25487,db = dbFacturas)
print (msj , dbFacturas)
msj , dbFacturas = facturas (1,2541,2,500000,db = dbFacturas)
print (msj , dbFacturas)
msj , dbFacturas = facturas (2,1429,5,25000.25487,db = dbFacturas)
print (msj , dbFacturas)
msj , dbFacturas = facturas (1,1429,1,700000,db = dbFacturas)
print (msj , dbFacturas)
msj , dbFacturas = facturas (2,1429,1,700000,db = dbFacturas)
print (msj , dbFacturas)
msj , dbFacturas = facturas (0,1429,1,700000,db = dbFacturas)
print (msj , dbFacturas)
msj , dbFacturas = facturas (0,1429, db = dbFacturas)
print (msj , dbFacturas)
msj , dbFacturas = facturas (1,1429,1,700000,db = dbFacturas)
print (msj , dbFacturas)
msj , dbFacturas = facturas (2,2541,1,274999.74513,db = dbFacturas)
print (msj , dbFacturas)
msj , dbFacturas = facturas (3,db = dbFacturas)
print (msj , dbFacturas)
