demanda = [24,26,22,25,19,31,26,18,29,24,39,23]

def forecast(demanda: list, rango_promedio: int, alpha: float) :
    suma = 0
    for i in range(0,rango_promedio - 1) :
        suma += demanda[i]
    promedio = suma / rango_promedio
    pronostico = [promedio]
    for i in range(rango_promedio,len(demanda) - 1) :
        D_t = alpha * demanda[i] + (1 - alpha) * pronostico[i - rango_promedio]
        pronostico += D_t
    return pronostico

pronostico = forecast(demanda, 2, 0.6)
print(pronostico)