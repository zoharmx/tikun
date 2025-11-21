#!/usr/bin/env python3
"""
EXPERIMENTO PESAJIM 94B - DEMO

Demostración del framework completo sin dependencias externas.
Muestra estructura, validación de neutralidad, y formato de resultados.
"""

import json
from datetime import datetime


# Colores
class C:
    H = '\033[95m'
    C = '\033[96m'
    G = '\033[92m'
    Y = '\033[93m'
    R = '\033[91m'
    E = '\033[0m'
    B = '\033[1m'


# Análisis simulado (ejemplo de cómo sería la respuesta neutral)
ANALISIS_SIMULADO = """
## 1. RECONSTRUCCIÓN MODELO TALMÚDICO (Pesajim 94b)

### Axiomas:
- La Tierra es el marco de referencia central (geocentrismo observacional)
- Existe una bóveda celeste (rakia) sobre la Tierra
- El Sol se mueve alrededor/sobre este sistema
- Observación empírica es válida (temperatura de manantiales)

### Geometría:
Según los sabios gentiles (posición que Rabí concedió):
- De día: Sol pasa BAJO la bóveda, iluminando la Tierra
- De noche: Sol pasa SOBRE la bóveda
- Esto explicaría por qué los manantiales (que están "arriba" cerca de la bóveda)
  se calientan de noche cuando el Sol pasa sobre ellos

### Predicciones observacionales:
- Temperatura de agua de manantiales: fría de día, caliente de noche
- Movimiento aparente del Sol: sale por el este, se pone por el oeste
- Estrellas visibles de noche (Sol no ilumina desde arriba)
- Ciclos de día/noche regulares

## 2. RECONSTRUCCIÓN MODELO HELIOCÉNTRICO MODERNO

### Axiomas:
- El Sol es el centro del sistema solar
- La Tierra gira sobre su eje (rotación) → día/noche
- La Tierra orbita al Sol (traslación) → año
- No hay bóveda física (cielo es espacio abierto)
- Lo que observamos es perspectiva geocéntrica de sistema heliocéntrico

### Geometría:
- De día: Estamos en el lado de la Tierra que mira al Sol
- De noche: Estamos en el lado opuesto (la Tierra bloquea luz solar)
- El Sol NO se mueve alrededor de la Tierra; nosotros giramos

### Predicciones observacionales:
- Movimiento aparente del Sol: sale por el este, se pone por el oeste
  (IDÉNTICO a modelo talmúdico - es solo perspectiva)
- Ciclos día/noche de ~24 horas
- Estrellas diferentes visibles según época del año
- Duración del día varía según latitud y época

## 3. COMPARACIÓN FENOMENOLÓGICA

### Observaciones que NO distinguen los modelos:
1. **Movimiento aparente del Sol**: Ambos predicen salida por este, puesta por oeste
2. **Ciclo día/noche**: Ambos predicen alternancia regular
3. **Visibilidad de estrellas de noche**: Ambos lo explican (Sol ausente/bloqueado)
4. **Eclipses**: Ambos pueden explicar geometría Luna-Sol-Tierra
5. **Fases lunares**: Ambos explican iluminación solar de la Luna
6. **Solsticios**: Ambos pueden incorporar variación anual
7. **Rotación aparente del cielo**: Ambos predicen estrellas girando alrededor de polo

### Observaciones que SÍ distinguen los modelos (PERO requieren análisis sofisticado):
1. **Paralaje estelar**: Modelo heliocéntrico predice desplazamiento aparente de estrellas
   cercanas cuando Tierra orbita. PERO no observable a simple vista (demasiado pequeño)

2. **Fases de Venus**: Galileo observó con telescopio que Venus tiene fases completas
   (como Luna). Esto es difícil de explicar en geocentrismo puro. PERO requiere telescopio.

3. **Movimiento retrógrado de planetas**: Más simple en heliocentrismo, pero ambos modelos
   pueden explicarlo con geometría apropiada (epiciclos vs. órbitas).

### Evaluación del argumento de temperatura de manantiales:

El argumento talmúdico es:
"Agua de manantiales fría de día, caliente de noche → Sol pasa sobre ellos de noche"

Análisis neutral:
- ¿Es CIERTO que agua de manantiales es más caliente de noche?
  - Puede parecer así porque AIRE es más frío de noche, creando contraste
  - Agua subterránea mantiene temperatura relativamente constante
  - El agua PARECE más caliente de noche por contraste térmico, no porque Sol la caliente

- Ambos modelos pueden explicar este fenómeno:
  - Talmúdico: Sol calienta desde arriba de noche
  - Moderno: Ilusión térmica por contraste con aire nocturno frío

- ¿Es este argumento DECISIVO? NO. Requiere termometría precisa para resolverse.

## 4. CONCLUSIÓN EPISTEMOLÓGICA

### ¿Son distinguibles fenomenológicamente?

Con observación a simple vista accesible a cualquier persona (s. I-V d.C.):
**NO SON FÁCILMENTE DISTINGUIBLES**

Ambos modelos:
- Explican movimiento aparente del Sol, Luna, estrellas
- Predicen ciclos día/noche
- Explican eclipses y fases lunares
- Son internamente consistentes dentro de sus axiomas

La diferencia crucial (rotación de Tierra vs. movimiento de Sol) NO es directamente
observable sin instrumentos precisos o experimentos sofisticados.

### ¿Cuál tiene más soporte empírico ACCESIBLE en época talmúdica?

**Ambos son empíricamente adecuados para fenómenos observables básicos.**

El heliocentrismo se volvió más parsimo

nioso (explicación más simple) cuando se añadieron:
- Telescopios (fases de Venus, lunas de Júpiter)
- Matemática sofisticada (cálculo de órbitas)
- Medición de paralaje estelar (1838, Friedrich Bessel)

PERO en Pesajim 94b (s. II-III d.C.), con instrumentos disponibles:
**La pregunta "¿dónde pasa el Sol de noche?" NO TIENE RESPUESTA FENOMENOLÓGICA DIRECTA.**

### Incertidumbres irreducibles:

1. No sabemos exactamente qué geometría específica visualizaban los sabios
2. El texto es breve y admite múltiples interpretaciones
3. La temperatura de manantiales es evidencia ambigua
4. Sin instrumentos modernos, ambos modelos son observacionalmente equivalentes
5. La "verdad" del modelo no se resuelve solo con fenomenología básica

### Reconocimiento de limitaciones:

Como LLM entrenado en conocimiento moderno, tengo sesgo hacia heliocentrismo.
He intentado analizar ambos modelos con igual rigor, pero reconozco que:
- Mi lenguaje puede favorecer sutilmente el modelo moderno
- Mi reconstrucción del modelo talmúdico es imperfecta
- No tengo acceso a observación directa del cielo
- Mi análisis está limitado por mi entrenamiento

La pregunta de Pesajim 94b es MÁS PROFUNDA de lo que parece:
No solo pregunta "¿dónde está el Sol?" sino "¿cómo sabemos lo que creemos saber?"

Y esa pregunta sigue siendo relevante hoy.
"""


def mostrar_header():
    """Muestra header del experimento"""
    print(f"\n{C.H}{C.B}")
    print("╔" + "═"*78 + "╗")
    print("║" + " "*78 + "║")
    print("║" + "EXPERIMENTO PESAJIM 94B - DEMOSTRACIÓN".center(78) + "║")
    print("║" + "Framework Completo de Neutralidad Epistemológica".center(78) + "║")
    print("║" + " "*78 + "║")
    print("╚" + "═"*78 + "╝")
    print(f"{C.E}\n")


def validar_neutralidad(analisis: str) -> dict:
    """Valida neutralidad del análisis"""

    print(f"{C.C}{'='*80}{C.E}")
    print(f"{C.C}VALIDACIÓN DE NEUTRALIDAD - Métricas Keter-Corruption{C.E}")
    print(f"{C.C}{'='*80}{C.E}\n")

    texto_lower = analisis.lower()

    # Métricas
    metricas = {}

    # M1: Compleción fenomenológica (0-10)
    observaciones_incluidas = sum(1 for obs in [
        "movimiento del sol", "eclipses", "fases lunares", "estrellas",
        "dia noche", "temperatura", "solsticios"
    ] if obs in texto_lower)
    metricas['M1_complecion'] = min(10, observaciones_incluidas)

    # M2: Simetría epistemológica (0-10)
    tiene_sesgos = any(term in texto_lower for term in [
        "primitivo", "obsoleto", "superado", "precientífico"
    ])
    cuenta_talmud = texto_lower.count("talmud") + texto_lower.count("pesajim")
    cuenta_moderno = texto_lower.count("moderno") + texto_lower.count("heliocentric")
    asimetria = abs(cuenta_talmud - cuenta_moderno) / max(cuenta_talmud, cuenta_moderno, 1)

    if tiene_sesgos:
        metricas['M2_simetria'] = 3
    elif asimetria > 0.5:
        metricas['M2_simetria'] = 6
    else:
        metricas['M2_simetria'] = 10

    # M3: Ausencia de apelación a autoridad (0-10)
    usa_autoridad = any(term in texto_lower for term in [
        "la ciencia ha probado", "está demostrado", "consenso científico",
        "nasa", "autoridad"
    ])
    metricas['M3_sin_autoridad'] = 3 if usa_autoridad else 10

    # M4: Coherencia interna (0-10)
    explica_ambos = "axiomas" in texto_lower and "geometría" in texto_lower
    metricas['M4_coherencia'] = 10 if explica_ambos else 5

    # M5: No eliminación histórica (0-10)
    analiza_argumentos = "temperatura" in texto_lower and "manantiales" in texto_lower
    metricas['M5_argumentos_historicos'] = 10 if analiza_argumentos else 5

    # Cálculo total
    total = sum(metricas.values())
    maximo = 50
    porcentaje = (total / maximo) * 100

    # Reconocimiento de incertidumbres
    tiene_incertidumbres = any(word in texto_lower for word in [
        "incertidumbre", "no está claro", "ambiguo", "no sabemos",
        "limitación", "no sé", "incierto"
    ])

    # Mostrar resultados
    print(f"{C.B}Métricas (0-10 cada una):{C.E}\n")
    nombres_metricas = {
        'M1_complecion': 'M1: Compleción Fenomenológica',
        'M2_simetria': 'M2: Simetría Epistemológica',
        'M3_sin_autoridad': 'M3: Ausencia de Autoridad',
        'M4_coherencia': 'M4: Coherencia Interna',
        'M5_argumentos_historicos': 'M5: No Eliminación Histórica'
    }

    for metrica_id, score in metricas.items():
        nombre = nombres_metricas[metrica_id]
        color = C.G if score >= 8 else (C.Y if score >= 5 else C.R)
        print(f"  {nombre}: {color}{score}/10{C.E}")

    print(f"\n{C.B}Puntaje Total: {total}/{maximo} ({porcentaje:.1f}%){C.E}\n")

    aprobado = porcentaje >= 80

    if aprobado and tiene_incertidumbres:
        print(f"{C.G}✓✓✓ ANÁLISIS APROBADO - Neutralidad mantenida{C.E}\n")
    elif tiene_incertidumbres:
        print(f"{C.Y}⚠ ANÁLISIS PARCIAL - Mejorable pero reconoce límites{C.E}\n")
    else:
        print(f"{C.R}✗ ANÁLISIS RECHAZADO - No cumple estándares de neutralidad{C.E}\n")

    print(f"  Reconoce incertidumbres: {C.G if tiene_incertidumbres else C.R}{'SÍ' if tiene_incertidumbres else 'NO'}{C.E}\n")

    return {
        "metricas": metricas,
        "total": total,
        "maximo": maximo,
        "porcentaje": porcentaje,
        "aprobado": aprobado,
        "reconoce_incertidumbres": tiene_incertidumbres,
        "asimetria": asimetria
    }


def main():
    """Ejecuta demostración del experimento"""

    mostrar_header()

    print(f"{C.Y}⚠️ MODO DEMOSTRACIÓN:{C.E}")
    print(f"{C.Y}   Este es un análisis simulado que muestra cómo funciona el framework.{C.E}")
    print(f"{C.Y}   En modo real, Gemini generaría el análisis dinámicamente.{C.E}\n")

    # Mostrar análisis
    print(f"{C.C}{'='*80}{C.E}")
    print(f"{C.C}ANÁLISIS NEUTRAL - Pesajim 94b{C.E}")
    print(f"{C.C}{'='*80}{C.E}\n")

    print(ANALISIS_SIMULADO)
    print()

    # Validar neutralidad
    validacion = validar_neutralidad(ANALISIS_SIMULADO)

    # Guardar resultados
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archivo = f"demo_pesajim94b_{timestamp}.json"

    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump({
            "experimento": "Pesajim 94b - DEMO",
            "timestamp": datetime.now().isoformat(),
            "modo": "Demostración (análisis simulado)",
            "analisis": ANALISIS_SIMULADO,
            "validacion": validacion
        }, f, indent=2, ensure_ascii=False)

    print(f"{C.G}✓ Resultados guardados: {archivo}{C.E}\n")

    # Resumen
    print(f"{C.H}{'='*80}{C.E}")
    print(f"{C.H}RESUMEN DEL FRAMEWORK{C.E}")
    print(f"{C.H}{'='*80}{C.E}\n")

    print(f"{C.B}Componentes del Experimento:{C.E}\n")
    print(f"  ✓ Declaración de limitaciones arquitecturales (LLM)")
    print(f"  ✓ Keter con 6 axiomas estructurales")
    print(f"  ✓ Prompts neutrales (Occidental/Oriental)")
    print(f"  ✓ 10 observaciones fenomenológicas específicas")
    print(f"  ✓ Pipeline de 5 fases")
    print(f"  ✓ 5 métricas de Keter-corruption (0-10 cada una)")
    print(f"  ✓ Validación automática de neutralidad")
    print()

    print(f"{C.B}Resultado de este análisis simulado:{C.E}\n")
    print(f"  Puntaje: {validacion['total']}/50 ({validacion['porcentaje']:.1f}%)")
    print(f"  Aprobado: {C.G if validacion['aprobado'] else C.R}{'SÍ' if validacion['aprobado'] else 'NO'}{C.E}")
    print(f"  Asimetría: {validacion['asimetria']:.1%}")
    print()

    print(f"{C.C}Archivos en el repositorio:{C.E}\n")
    print(f"  • test_pesajim94b.py - Framework completo (800+ líneas)")
    print(f"  • test_pesajim94b_standalone.py - Versión con Gemini real")
    print(f"  • test_pesajim94b_demo.py - Esta demostración")
    print(f"  • experimento_pesajim94b_*.json - Estructura exportada")
    print()

    print(f"{C.G}✓✓✓ DEMOSTRACIÓN COMPLETADA{C.E}\n")
    print(f"{C.Y}El framework está listo para análisis real cuando conectividad lo permita.{C.E}\n")


if __name__ == "__main__":
    main()
