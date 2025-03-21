# Función para calcular el descuento

# Solicitar al usuario los valores 1 y 2
valor1= float(input("Ingrese el valor 1: "))
valor2= float(input("Ingrese el valor 2: "))

# Calculamos el total de la compra
total_compra = valor1 + valor2
print(f"el total de su compra es:{total_compra: .2f}")


#definimos la función
def calcular_descuento(total_compra,porcentaje_descuento=0.10):
    # Calculamos el descuento
    descuento=total_compra*porcentaje_descuento
    # Devolvemos el monto del descuento
    return descuento


# Llamada a la función con el monto total y el porcentaje de descuento (10%)
valor_descuento = calcular_descuento(total_compra)

# Calculamos el monto final a pagar después del descuento
monto_final = total_compra - valor_descuento
print()
# Mostrar resultados
print(f"su valor del 10% de descuento es: {valor_descuento:.2f}")
print(f"su monto final a pagar después del descuento: {monto_final: .2f}")
#preguntar al cliente si desea adquirir un descuento del 20%
print()
doble_descuento=str(input("desea adquirir un descuento del 20% SI/NO: "))
if doble_descuento.lower()=="si":
    print()
    #llamamos a la funcion por segunda ocasion para calcular el valor en este caso del 20%
    valor_descuento2=calcular_descuento(total_compra,0.20)
    #calculamos el precio final con el descuento del 20%
    monto_final2 = total_compra - valor_descuento2
    print(f"su valor del 20% de descuento es: {valor_descuento2:.2f}")
    print(f"su monto final a pagar es: {monto_final2:.2f}")
    print("gracias por su compra")
else:
    print()
    print("gracias por su compra")
