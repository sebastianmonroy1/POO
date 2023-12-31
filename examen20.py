# -*- coding: utf-8 -*-
"""EXAMEN20.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QbgGr_EMvxCOuGKLqesun5wBFzsrprRl
"""



"""**EXAMEN PARCIAL 2**

Ejercicio 1:
¿Qué es una clase y por qué es útil?
Define una clase con un ejemplo, dando todas sus características.

Una clase es como un plano o una plantilla que se utiliza en la programación para crear objetos. Estos objetos pueden representar cosas del mundo real y tener características (atributos) y comportamientos (métodos) específicos.
"""

class Coche:
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")


ferrari_enzo = Coche("Ferrari", "Enzo", 2003, "Rojo")
porsche_911 = Coche("Porsche", "911", 2022, "Azul")

ferrari_enzo.mostrar_informacion()
porsche_911.mostrar_informacion()

"""Ejercicio 2:
En Python, un constructor es un método especial que se llama automáticamente cuando se crea un objeto. Se utiliza para inicializar los atributos del objeto y realizar cualquier tarea de configuración necesaria antes de su uso.
Para este ejercicio contesta las siguientes preguntas:
¿Cuál es la sintaxis para definir un constructor dentro de una clase?
Considera el siguiente código:

La clase 'Human' tiene un constructor que toma dos parametros, ¿cuáles son?

La sintaxis correcta es __init__.
"""

class Human:
    def __init__(self):
        self.legs = 2
        self.arms = 2

"""La clase 'Human' tiene un constructor llamado __init__, que es un método especial en Python utilizado para configurar los objetos cuando se crean, en el codigo, el constructor toma un único parámetro llamado self, que se refiere al propio objeto.

Ejercicio 3:
Indica si las siguientes afirmaciones son verdaderas o falsas:
El primer parámetro del método '__ init() __' es siempre 'self' , que se refiere a la instancia de la clase que se está creando. Se pasa automáticamente al constructor cuando se instancia el objeto.
Después de 'self', puedes definir cualquier otro parámetro necesario para inicializar los atributos del objeto.
Cuando añades la función '__ init () __' , la clase heredada ya no hereda la función ' __ init () __ ' de la clase madre.
En la programación orientada a objetos, las clases pueden heredar atributos y métodos de otras clases.
Cuando hablamos de polimorfismos en Python, diferentes clases pueden ser tratadas como instancias de la misma superclase, independientemente de cómo implementen el mismo método.

1. VERDADERO: El primer parámetro del método __init__ en una clase de Python siempre es 'self', que se refiere a la instancia de la clase que se está creando.
2. VERDADERO: Después de 'self', puedes definir cualquier otro parámetro necesario para inicializar los atributos del objeto. Estos parámetros se pueden utilizar para personalizar la inicialización de la instancia.
3. FALSO: Cuando añades la función __init__, la clase heredada no anula la función __init__ de la clase madre por defecto.
4. VERDADERO: Las clases pueden heredar atributos y métodos de otras clases. La herencia es un concepto fundamental en la programación orientada a objetos, lo que permite que las clases compartan características de otras clases.
5. VERDADERO: Polimorfismo en Python, diferentes clases pueden ser tratadas como instancias de la misma superclase, independientemente de cómo implementen el mismo método.

Ejercicio 4: A partir de un diccionario, crea un DataFrame (que llamarás precios_muestra) que consista de dos columnas y que tenga 12 valores flotantes que eligirás de manera aleatoria en el intervalo (8,13). Etiqueta del 1 al 12 y llama a la columna de etiquetas Mes.
1.- Construye una función que calcule los rendimientos simples de cada columna.
2.- Las desviaciones estadísticas de los rendimientos ayudan a calcular la volatilidad del portafolio:
desviaciones=(rendimientos−media(rendimientos))2.
Crea una función que calcule la media de las desviaciones y luego la volatilidad de tu portafolio (raíz cuadrada de la media de las desviaciones).
3.- Anualizamos la volatilidad escalándola (multiplicándola) por la raíz cuadrada del número de períodos por observación.
Por lo tanto, para anualizar la volatilidad de una serie mensual, la multiplicamos por la raíz cuadrada de 12. Muestra la serie de la volatilidad anualizada.
4.- Realiza una gráfica de barras para los rendimientos y una gráfica en líneas para los precios.
5.- Calcula los rendimientos compuestos para cada columna y después anualiza los rendimientos.
"""

import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

#1

random.seed(42)
precios_muestra = pd.DataFrame({'Mes': range(1, 13),
                                'Precio': [random.uniform(8, 13) for _ in range(12)]})

#2

def calcular_rendimientos(df):
    df['Rendimiento'] = df['Precio'].pct_change() * 100
    return df

precios_muestra = calcular_rendimientos(precios_muestra)

#3

def calcular_volatilidad_anualizada(df):
    desviaciones = (df['Rendimiento'] - df['Rendimiento'].mean())**2
    volatilidad = np.sqrt(desviaciones.mean()) * np.sqrt(12)  # Multiplicar por la raíz cuadrada de 12 para anualizar
    return volatilidad

volatilidad_anualizada = calcular_volatilidad_anualizada(precios_muestra)

#4

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
precios_muestra.set_index('Mes')['Rendimiento'].plot(kind='bar', title='Rendimientos')
plt.subplot(1, 2, 2)
precios_muestra.set_index('Mes')['Precio'].plot(kind='line', title='Precios')
plt.show()

#5

def calcular_rendimientos_compuestos(df):
    df['Rendimiento_Compuesto'] = (1 + df['Rendimiento'] / 100).cumprod()
    rendimiento_anualizado = (df['Rendimiento_Compuesto'].iloc[-1])**(12/len(df)) - 1
    return rendimiento_anualizado

rendimiento_anualizado = calcular_rendimientos_compuestos(precios_muestra)

print("Volatilidad Anualizada:", volatilidad_anualizada)
print("Rendimiento Anualizado:", rendimiento_anualizado)

"""Ejercicio 5: Carga dos tickers y realiza los pasos del ejercicio anterior usando los tickers que elijas. Recuerda tomar en cuenta la ventana de tiempo que manejarás. Realiza un análisis estadístico (estadística descriptiva, histogramas y gráficas de series de tiempo)."""

pip install yfinance

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ticker1 = 'CRM'
ticker2 = 'NVDA'
start_date = '2022-01-01'
end_date = '2022-12-31'

data1 = yf.download(ticker1, start=start_date, end=end_date)['Adj Close']
data2 = yf.download(ticker2, start=start_date, end=end_date)['Adj Close']

precios = pd.DataFrame({ticker1: data1, ticker2: data2})

rendimientos = precios.pct_change().dropna()

volatilidad_anualizada = np.sqrt(252) * rendimientos.std()

#252 dias habiles

estadisticas_descriptivas = rendimientos.describe()

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
rendimientos[ticker1].hist(bins=30, alpha=0.5, label=ticker1)
rendimientos[ticker2].hist(bins=30, alpha=0.5, label=ticker2)
plt.legend()
plt.title('Histogramas de Rendimientos')
plt.subplot(1, 2, 2)
precios.plot(title='Series de Tiempo de Precios')
plt.show()

rendimiento_compuesto1 = (1 + rendimientos[ticker1]).prod() - 1
rendimiento_compuesto2 = (1 + rendimientos[ticker2]).prod() - 1

print("Volatilidad Anualizada", ticker1, ":", volatilidad_anualizada[ticker1])
print("Volatilidad Anualizada", ticker2, ":", volatilidad_anualizada[ticker2])
print("Rendimiento Anualizado", ticker1, ":", rendimiento_compuesto1)
print("Rendimiento Anualizado", ticker2, ":", rendimiento_compuesto2)