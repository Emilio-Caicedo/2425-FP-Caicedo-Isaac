# Desarrolla una función en Python que calcule la temperatura promedio de una ciudad durante un período de tiempo.
# Utiliza como base el ejemplo anterior, donde tenías datos de 3 ciudades durante 4 semanas.
# Tu función debe recibir estos datos como parámetros y calcular la temperatura promedio de cada ciudad.

temperaturas = [
    [   # Esmeraldas
        [   # Semana 1
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 23},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 23}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 27}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 23},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 26},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 25}
        ]
    ],
    [   # Ambato
        [   # Semana 1
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 10},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 10},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 9},
            {"day": "Domingo", "temp": 18}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 9},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 7},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 9}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 10},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 10},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 11},
            {"day": "Domingo", "temp": 18}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 10},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 10},
            {"day": "Domingo", "temp": 16}
        ]
    ],
    [   # Lago Agrio
        [   # Semana 1
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 21},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 24}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 31}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 26},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 25}
        ]
    ]
]

# Lista de nombres de ciudades en el mismo orden que en la lista de temperaturas.
ciudades = ["Esmeraldas", "Ambato", "Lago Agrio"]

# Función para calcular el promedio de temperatura de cada una de las 3 Ciudades durante el Mes (4 semanas)
def calcular_temperatura_promedio(temperaturas):
    """
    Calcula el promedio de temperaturas de cada ciudad durante 1 mes (4 semanas).

    :param temperaturas: Lista de listas con los datos de las temperaturas.
    :return: Diccionario con las ciudades y su temperatura promedio.
    """

    promedios = {}

    for i, ciudad in enumerate(temperaturas):
        total_temp = 0
        total_dias = 0

        # Acceder a la lista de las 4 semanas de cada ciudad.
        for semana in ciudad:
            for dia in semana:  # Cada semana es una lista de los 7 días.
                total_temp += dia["temp"]
                total_dias += 1

        # Calcular el promedio
        promedio_ciudad = total_temp / total_dias
        promedios[ciudades[i]] = round(promedio_ciudad, 2)

    return promedios

# Llamar a la función y mostrar los resultados
resultados = calcular_temperatura_promedio(temperaturas)

print("\nPromedio de Temperaturas por Ciudad: ")
for ciudad, promedio in resultados.items():
    print(f"{ciudad}: {promedio}°C")