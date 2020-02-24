consumo = 0
descuento10 = 0.9
descuento20 = 0.8
descuento30 = 0.7
impuesto = 1.19

consumo = input("Cuánto ha consumido usted? ")

if float(consumo) < 100.0 :
    consumo = float(consumo) * float(descuento10) * float(impuesto)

elif float(consumo) < 200.0 and float(consumo) > 100.0:
    consumo = float(consumo) * float(descuento20) * float(impuesto)

elif float(consumo) > 200:
    consumo = float(consumo) * float(descuento30) * float(impuesto)
    

print("Tras aplicar el impuesto y el descuento su cuenta queda: ")
print(consumo)