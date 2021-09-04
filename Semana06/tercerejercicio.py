x =1
while x == 1:

    compra =float(input("valor de la compra:"))
    tipo = str(input("pagaris al contado o con targeta de credito:"))
    if tipo == "contado":
        descuento = compra *0.05
        compra = compra - descuento
        print("se agrego descuento:",compra)
    elif tipo =="targeta de credito":
        aumento = compra *0.03
        compra = compra  + aumento
        print("se aplico aumento:", compra)

    else:
        print("no seleccionaste ninguna de las opcion")
        
        x += 2