def sumar(a, b):
    """Retorna la suma de dos números."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Ambos argumentos deben ser números.")
    return a + b

def multiplicar(a, b):
    """Retorna la multiplicación de dos números."""
    return a * b