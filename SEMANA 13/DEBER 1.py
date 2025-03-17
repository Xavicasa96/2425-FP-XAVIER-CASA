# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (CUENCA, LOJA, MANTA)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas)
temperaturas = [
    [   # CUENCA
        [   # Semana 1
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 21},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 12},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 16}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 13}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 11},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 11},
            {"day": "Domingo", "temp": 15}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 10},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 11}
        ]
    ],
    [   # LOJA
        [   # Semana 1
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 19}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 13},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 11}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 20}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 11},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 20}
        ]
    ],
    [   # MANTA
        [   # Semana 1
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 22}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 21}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 23}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 23},
            {"day": "Domingo", "temp": 20}
        ]
    ]
]


def calcular_temperatura_promedio(temperaturas):
    ciudades = ["CUENCA", "LOJA", "MANTA"]
    promedios = {}

    # Iteramos por cada ciudad
    for i, ciudad in enumerate(temperaturas):
        suma_temperaturas = 0
        total_dias = 0

        # Iteramos por las semanas de la ciudad
        for semana in ciudad:
            # Iteramos por los días de la semana
            for dia in semana:
                suma_temperaturas += dia["temp"]
                total_dias += 1

        # Calculamos el promedio y lo agregamos al diccionario
        promedios[ciudades[i]] = suma_temperaturas / total_dias

    return promedios


# Usamos la función con los datos de las temperaturas
promedios = calcular_temperatura_promedio(temperaturas)
print(promedios)



