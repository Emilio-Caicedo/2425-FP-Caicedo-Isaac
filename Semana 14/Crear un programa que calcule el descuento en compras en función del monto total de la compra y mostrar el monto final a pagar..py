# El objetivo de esta tarea es practicar el uso de funciones en Python, incluyendo parámetros, valores predeterminados y retorno de valores.
# Deberás crear un programa que calcule el descuento en compras en función del monto total de la compra y mostrar el monto final a pagar.

# Creación de la Función:
    # Crea una función llamada calcular_descuento que tome dos parámetros: el monto total de la compra y un valor predeterminado para el porcentaje de descuento.
    # La función debe calcular el descuento aplicando el porcentaje al monto total de la compra.
    # La función debe devolver el monto del descuento calculado.

def calcular_descuento(precio_total, porcentaje_descuento = 15):
    """
    Calcula el monto del descuento en función del porcentaje dado.
    :param precio_total: float - Total a Pagar de la Compra
    :param porcentaje_descuento: float - Porcentaje de Descuento (por defecto es 15%)
    :return: float - Monto del Descuento
    """
    descuento = (precio_total * porcentaje_descuento) / 100

    return descuento

# Llamada a la Función:
    # Llama a la función calcular_descuento al menos dos veces desde el programa principal.
    # En una llamada, proporciona el monto total de la compra y, en la otra, proporciona tanto el monto total de la compra como el porcentaje de descuento.

precio1 = 450.00
precio2 = 860.00
porcentaje_descuento2 = 30

descuento1 = calcular_descuento(precio1)
descuento2 = calcular_descuento(precio2, porcentaje_descuento2)

# Cálculo del Total Final a Pagar
precio_final1 = precio1 - descuento1
precio_final2 = precio2 - descuento2

# Mostrar el Total a Pagar con el Descuento
print(f"Compra 1: Precio Total ${precio1:.2f}, Descuento: ${descuento1:.2f}, Total a Pagar: ${precio_final1:.2f}")
print(f"Compra 2: Precio Total ${precio2:.2f}, Descuento: ${descuento2:.2f}, Total a Pagar: ${precio_final2:.2f}")