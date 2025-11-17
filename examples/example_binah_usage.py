"""
Ejemplo de uso de Binah (Entendimiento) - Analisis Contextual Profundo

Este ejemplo muestra como usar Binah para analizar las implicaciones
contextuales de decisiones complejas con multiples stakeholders.
"""

import sys
import os

# Agregar el directorio raiz al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.sefirot.binah import Binah
from src.sefirot.chochmah_gemini import ChochmahGemini
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()


def example_policy_analysis():
    """
    Ejemplo: Analisis de una politica publica

    Una ciudad esta considerando implementar transporte publico gratuito.
    Queremos entender las implicaciones contextuales profundas.
    """
    print("=" * 80)
    print("EJEMPLO: Analisis Contextual de Politica Publica")
    print("=" * 80)

    # Crear Sefirot
    chochmah = ChochmahGemini()
    binah = Binah()

    # La pregunta
    query = """
    Una ciudad de 500,000 habitantes esta considerando hacer el transporte publico
    completamente gratuito, eliminando todas las tarifas. Esto se financiaria
    con un pequeño aumento en impuestos locales.

    Cuales son las implicaciones profundas de esta decision?
    """

    print(f"\nPREGUNTA:\n{query}\n")

    # PASO 1: Chochmah razona
    print("-" * 80)
    print("PASO 1: Chochmah (Sabiduria) - Razonamiento Profundo")
    print("-" * 80)

    chochmah_result = chochmah.process({
        'query': query,
        'objective': 'Maximizar bienestar comunitario y sostenibilidad'
    })

    print(f"\nNivel de Confianza: {chochmah_result['confidence_level']:.2f}")
    print(f"\nComprension del Problema:")
    print(chochmah_result['understanding'][:400] + "...\n")

    print(f"Insights Clave:")
    print(chochmah_result['insights'][:600] + "...\n")

    # PASO 2: Binah analiza contexto
    print("-" * 80)
    print("PASO 2: Binah (Entendimiento) - Analisis Contextual Profundo")
    print("-" * 80)

    binah_result = binah.process({
        'chochmah_output': chochmah_result,
        'query': query
    })

    # Mostrar analisis contextual
    print("\n>>> CONTEXTO HISTORICO:")
    print(binah_result['historical_context'][:500] + "...\n")

    print(">>> STAKEHOLDERS AFECTADOS:")
    print(binah_result['stakeholders'][:600] + "...\n")

    print(">>> EFECTOS DE PRIMER ORDEN (Inmediatos):")
    print(binah_result['first_order_effects'][:400] + "...\n")

    print(">>> EFECTOS DE SEGUNDO ORDEN (Reacciones y cambios sistemicos):")
    print(binah_result['second_order_effects'][:600] + "...\n")

    print(">>> EFECTOS DE TERCER ORDEN (Largo plazo, emergentes):")
    print(binah_result['third_order_effects'][:600] + "...\n")

    print(">>> RIESGOS SISTEMICOS:")
    print(binah_result['systemic_risks'][:500] + "...\n")

    print(">>> CONSIDERACIONES ETICAS:")
    print(binah_result['ethical_considerations'][:500] + "...\n")

    print(">>> SINTESIS CONTEXTUAL:")
    print(binah_result['contextual_synthesis'][:700] + "...\n")

    print("-" * 80)
    print("METRICAS DE BINAH:")
    print("-" * 80)
    print(f"Perspectivas consideradas: {binah_result['perspectives_count']}")

    alignment = binah.validate_alignment()
    print(f"Profundidad contextual: {alignment['contextual_depth_score']:.2f}")
    print(f"Status de alineamiento: {alignment['status']}")


def example_business_decision():
    """
    Ejemplo: Decision empresarial con dilemas eticos

    Una empresa de tecnologia debe decidir sobre el uso de datos de usuarios.
    """
    print("\n\n" + "=" * 80)
    print("EJEMPLO: Decision Empresarial con Dilemas Eticos")
    print("=" * 80)

    # Solo Binah, con insights pre-generados
    binah = Binah()

    # Simulamos que ya tenemos insights de Chochmah
    insights = """
    Los datos de comportamiento de usuarios pueden generar valor economico
    significativo, pero plantean dilemas de privacidad y consentimiento.

    Existe tension entre:
    - Maximizar valor para accionistas
    - Respetar privacidad y autonomia de usuarios
    - Cumplir con regulaciones
    - Mantener confianza publica
    """

    query = """
    Una empresa de redes sociales tiene datos detallados de comportamiento
    de 100 millones de usuarios. Puede monetizar estos datos vendiendolos
    a terceros o usarlos para publicidad dirigida mas efectiva.

    Cual es el camino correcto?
    """

    print(f"\nSITUACION:\n{query}\n")

    binah_result = binah.process({
        'insights': insights,
        'query': query,
        'objective': 'Maximizar Tikun Olam (bienestar general con respeto a dignidad)'
    })

    print("-" * 80)
    print("ANALISIS CONTEXTUAL DE BINAH:")
    print("-" * 80)

    print("\n>>> STAKEHOLDERS (quien esta afectado?):")
    print(binah_result['stakeholders'][:700] + "...\n")

    print(">>> EFECTOS DE SEGUNDO ORDEN:")
    print(binah_result['second_order_effects'][:600] + "...\n")

    print(">>> RIESGOS SISTEMICOS:")
    print(binah_result['systemic_risks'][:600] + "...\n")

    print(">>> CONSIDERACIONES ETICAS:")
    print(binah_result['ethical_considerations'][:800] + "...\n")

    print(">>> SINTESIS CONTEXTUAL:")
    print(binah_result['contextual_synthesis'][:700] + "...\n")

    print("-" * 80)
    print(f"Perspectivas analizadas: {binah_result['perspectives_count']}")


def example_custom_temperature():
    """
    Ejemplo: Ajustar temperatura de Binah para diferentes tipos de analisis
    """
    print("\n\n" + "=" * 80)
    print("EJEMPLO: Ajuste de Temperatura de Binah")
    print("=" * 80)

    # Crear Binah con temperatura personalizada
    binah_conservative = Binah()
    binah_conservative.set_temperature(0.3)  # Mas conservadora, menos creativa

    binah_exploratory = Binah()
    binah_exploratory.set_temperature(1.2)  # Mas explorativa

    insights = """
    La inteligencia artificial podria reemplazar el 40% de los trabajos
    actuales en los proximos 20 anos.
    """

    print("\nAnalisis con TEMPERATURA BAJA (0.3) - Conservador:")
    print("-" * 80)

    result_conservative = binah_conservative.process({
        'insights': insights,
        'query': 'Que debemos hacer ante la automatizacion laboral?'
    })

    print(result_conservative['contextual_synthesis'][:500] + "...\n")

    print("\nAnalisis con TEMPERATURA ALTA (1.2) - Exploratorio:")
    print("-" * 80)

    result_exploratory = binah_exploratory.process({
        'insights': insights,
        'query': 'Que debemos hacer ante la automatizacion laboral?'
    })

    print(result_exploratory['contextual_synthesis'][:500] + "...\n")


if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("EJEMPLOS DE USO DE BINAH (ENTENDIMIENTO)")
    print("=" * 80)

    # Ejemplo 1: Politica Publica
    example_policy_analysis()

    # Ejemplo 2: Decision Empresarial
    example_business_decision()

    # Ejemplo 3: Temperatura Personalizada
    example_custom_temperature()

    print("\n" + "=" * 80)
    print("FIN DE EJEMPLOS")
    print("=" * 80)
