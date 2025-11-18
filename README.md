# Proyecto de Ciclo CI/CD

Este repositorio contiene la demostración práctica del ciclo de Integración Continua (CI) y Entrega Continua (CD) hasta la construcción de un paquete de software. He configurado un pipeline usando **GitHub Actions** para automatizar los procesos de prueba y empaquetado, cumpliendo con los requisitos del ejercicio.

---

## 1. Mi Entendimiento del Ciclo CI/CD

El objetivo principal de esta práctica era automatizar las fases clave del desarrollo.

### Integración Continua (CI)
Para mí, CI significa que cada vez que subo código, mi sistema automatizado lo construye y, lo más importante, **ejecuta mis pruebas**. Esto me ayuda a detectar fallos rápidamente antes de que se conviertan en un problema grande.

### Entrega Continua (CD)
En este proyecto, mi fase de CD se centra en la **creación del paquete (package)**. Una vez que las pruebas pasan en CI, el sistema compila y prepara el artefacto final (`.whl` y `.tar.gz`) que podría ser distribuido o desplegado.

---

## 2. Componentes de Mi Aplicación

Mi ejemplo práctico es una librería simple en Python para operaciones matemáticas básicas que usé para demostrar el pipeline.

### A. Archivo Principal: `app.py`

Aquí está la lógica que escribí para las operaciones:

```python
# app.py
def sumar(a, b):
    """Retorna la suma de dos números."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        # Me aseguré de que solo acepte números y lance un error si no es así.
        raise TypeError("Ambos argumentos deben ser números.")
    return a + b

def multiplicar(a, b):
    """Retorna la multiplicación de dos números."""
    return a * b