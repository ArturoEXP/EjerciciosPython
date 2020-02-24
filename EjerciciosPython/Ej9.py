consumo = 0
descuento10 = 0.9
descuento20 = 0.8
impuesto = 1.19

consumo = input("Cuánto ha consumido usted? ")

if ( float(consumo) < 100.0 ):
    consumo = float(consumo) * float(descuento10) * float(impuesto)
else:
    consumo = float(consumo) * float(descuento20) * float(impuesto)

print("Tras aplicar el impuesto y el descuento su cuenta queda: ")
print(consumo)