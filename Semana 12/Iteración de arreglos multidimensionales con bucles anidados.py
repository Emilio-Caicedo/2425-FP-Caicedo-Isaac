# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
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

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Esmeraldas", "Ambato", "Lago Agrio"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}: ")
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f" Semana {semana_idx + 1}: {promedio:.2f} °C")