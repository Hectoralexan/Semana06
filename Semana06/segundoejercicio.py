#Si gasto hasta $100, pago con dinero en efectivo. Si no, si gasto más de $100 pero menos de $300, pago con tarjeta de débito. Si no, pago con
#tarjeta de crédito
compra = int(input("coloque el dato de su compra: "))
#vamos a comprar los datos 
#si es manor o igual a 100 
#se pagaria en efectivo
if compra <= 100: 
 print ("Pago en efectivo")
#vamos a evaluar otra condicion
#lo vamos a comparar con and 
elif compra > 100 and compra < 300: 
 print ("Pago con tarjeta de débito")
#si culquiera de las condiciones anteriores no se cumplen pasaria al else
else: 
 print ("Pago con tarjeta de crédito")