"""
Demo de Chochmah (Sabiduría)
Demuestra uso de razonamiento profundo con Claude API

IMPORTANTE: Requiere ANTHROPIC_API_KEY en archivo .env
"""

import sys
import os
from pathlib import Path

# Agregar path del proyecto
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.sefirot.chochmah import Chochmah
from src.sefirot.keter import Keter
from dotenv import load_dotenv
from loguru import logger

# Configurar logger
logger.add(
    "logs/chochmah_demo.log",
    rotation="1 MB",
    level="DEBUG"
)


def demo_basic_query():
    """Demo 1: Consulta básica a Chochmah"""
    print("\n" + "="*70)
    print("DEMO 1: Consulta Básica a Chochmah")
    print("="*70)

    chochmah = Chochmah()

    query_data = {
        'query': '''
        ¿Cómo puede la inteligencia artificial contribuir a Tikún Olam
        (reparación del mundo) sin crear nuevos problemas?
        ''',
        'context': '''
        Estamos en 2025, con aceleración tecnológica observable.
        IAG podría surgir antes de 2030.
        Necesitamos alineamiento antes de ese punto.
        ''',
        'objective': 'Maximizar Tikún Olam - florecimiento de toda la creación'
    }

    print("\nProcesando consulta profunda con Claude...")

    result = chochmah.process(query_data)

    if result['processing_successful']:
        print(f"\n{'='*70}")
        print("COMPRENSIÓN:")
        print(f"{'='*70}")
        print(result['understanding'])

        print(f"\n{'='*70}")
        print("ANÁLISIS:")
        print(f"{'='*70}")
        print(result['analysis'])

        print(f"\n{'='*70}")
        print("INSIGHTS:")
        print(f"{'='*70}")
        print(result['insights'])

        print(f"\n{'='*70}")
        print("INCERTIDUMBRES:")
        print(f"{'='*70}")
        print(result['uncertainties'])

        print(f"\n{'='*70}")
        print("RECOMENDACIÓN:")
        print(f"{'='*70}")
        print(result['recommendation'])

        print(f"\n{'='*70}")
        print(f"NIVEL DE CONFIANZA: {result['confidence_level']:.2f}")
        print(f"{'='*70}")
    else:
        print(f"\nError: {result['error']}")


def demo_keter_chochmah_integration():
    """Demo 2: Integración Keter → Chochmah"""
    print("\n" + "="*70)
    print("DEMO 2: Integración Keter → Chochmah")
    print("="*70)

    # Inicializar Sefirot
    keter = Keter()
    chochmah = Chochmah()

    # Conectar Keter con Chochmah
    keter.connect_to(chochmah, "to_wisdom")

    print("\nKeter evaluando acción propuesta...")

    # Acción propuesta
    proposed_action = {
        'action': 'Desarrollar sistema de IA para optimizar distribución de recursos médicos',
        'context': 'Escasez de recursos en hospitales durante crisis',
        'expected_outcome': 'Reducir muertes evitables mediante mejor asignación de recursos'
    }

    # Keter evalúa alineamiento
    keter_evaluation = keter.process(proposed_action)

    print(f"\nKeter Evaluación:")
    print(f"  Alineada: {keter_evaluation['aligned']}")
    print(f"  Score: {keter_evaluation['alignment_score']:.2f}")
    print(f"  Razonamiento: {keter_evaluation['reasoning'][:200]}...")

    if keter_evaluation['aligned']:
        print("\n✓ Keter aprueba - Enviando a Chochmah para razonamiento profundo...")

        # Preparar consulta para Chochmah
        chochmah_query = {
            'query': f"Analiza esta acción: {proposed_action['action']}",
            'context': f"{proposed_action['context']}. Keter ha evaluado esto como alineado con Tikún Olam.",
            'objective': 'Maximizar Tikún Olam'
        }

        result = chochmah.process(chochmah_query)

        if result['processing_successful']:
            print(f"\nChochmah - INSIGHTS CLAVE:")
            print(result['insights'][:300] + "...")

            print(f"\nChochmah - INCERTIDUMBRES IDENTIFICADAS:")
            print(result['uncertainties'][:300] + "...")
        else:
            print(f"\nError en Chochmah: {result['error']}")
    else:
        print("\n✗ Keter rechaza - No pasa a Chochmah")
        print("Modificaciones sugeridas:")
        for mod in keter_evaluation['suggested_modifications']:
            print(f"  - {mod}")


def demo_epistemic_humility():
    """Demo 3: Humildad Epistémica de Chochmah"""
    print("\n" + "="*70)
    print("DEMO 3: Humildad Epistémica")
    print("="*70)

    chochmah = Chochmah()

    # Consulta deliberadamente ambigua
    ambiguous_query = {
        'query': '''
        ¿Cuál es el mejor sistema económico para maximizar bienestar humano?
        ''',
        'context': 'Considerando toda la historia humana',
        'objective': 'Maximizar Tikún Olam'
    }

    print("\nProcesando consulta ambigua (debería reconocer incertidumbre)...")

    result = chochmah.process(ambiguous_query)

    if result['processing_successful']:
        print(f"\nNivel de Confianza: {result['confidence_level']:.2f}")

        print(f"\n{'='*70}")
        print("INCERTIDUMBRES RECONOCIDAS:")
        print(f"{'='*70}")
        print(result['uncertainties'])

        # Validar alineamiento (debería detectar humildad)
        validation = chochmah.validate_alignment()

        print(f"\n{'='*70}")
        print("VALIDACIÓN DE ALINEAMIENTO:")
        print(f"{'='*70}")
        print(f"  Alineada: {validation['is_aligned']}")
        print(f"  Activaciones totales: {validation['total_activations']}")
        print(f"  Reconocimientos de incertidumbre: {validation['uncertainty_acknowledgments']}")
        print(f"  Ratio de humildad epistémica: {validation['epistemic_humility_ratio']:.2f}")
        print(f"  Status: {validation['status']}")


def demo_model_configuration():
    """Demo 4: Configuración de Modelos"""
    print("\n" + "="*70)
    print("DEMO 4: Configuración de Modelos y Temperatura")
    print("="*70)

    chochmah = Chochmah()

    print(f"\nConfiguración inicial:")
    print(f"  Modelo: {chochmah.model}")
    print(f"  Temperatura: {chochmah.temperature}")
    print(f"  Max tokens: {chochmah.max_tokens}")

    # Cambiar a temperatura más determinista
    print(f"\nCambiando temperatura a 0.3 (más determinista)...")
    chochmah.set_temperature(0.3)

    print(f"  Nueva temperatura: {chochmah.temperature}")

    # Ejemplo de consulta con baja temperatura
    query = {
        'query': '¿Qué es 2+2?',
        'context': 'Matemáticas básicas',
        'objective': 'Respuesta precisa'
    }

    print("\nProcesando consulta simple con temperatura baja...")
    result = chochmah.process(query)

    if result['processing_successful']:
        print(f"\nRespuesta (debería ser muy directa):")
        print(result['analysis'][:200])


def demo_metrics():
    """Demo 5: Métricas de Desempeño"""
    print("\n" + "="*70)
    print("DEMO 5: Métricas de Desempeño")
    print("="*70)

    chochmah = Chochmah()

    # Procesar varias consultas
    queries = [
        {'query': 'Pregunta 1: ¿Qué es Tikún Olam?'},
        {'query': 'Pregunta 2: ¿Cómo funciona la IA?'},
        {'query': 'Pregunta 3: ¿Qué es la ética?'}
    ]

    print(f"\nProcesando {len(queries)} consultas...")

    for i, query in enumerate(queries, 1):
        print(f"  {i}. Procesando...")
        result = chochmah.process(query)

        if not result['processing_successful']:
            print(f"     Error: {result['error']}")

    # Obtener métricas
    metrics = chochmah.get_metrics()

    print(f"\n{'='*70}")
    print("MÉTRICAS DE CHOCHMAH:")
    print(f"{'='*70}")
    print(f"  Sefirá: {metrics['sefira']}")
    print(f"  Posición: {metrics['position']}")
    print(f"  Activaciones: {metrics['activations']}")
    print(f"  Tiempo total de procesamiento: {metrics['total_processing_time']:.2f}s")
    print(f"  Tiempo promedio por activación: {metrics['average_processing_time']:.2f}s")
    print(f"  Tasa de éxito: {metrics['success_rate']:.2%}")
    print(f"  Canales conectados: {metrics['connected_channels']}")


def main():
    """Ejecuta todas las demos"""

    # Cargar variables de entorno
    load_dotenv()

    # Verificar que existe API key
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("\n" + "="*70)
        print("ERROR: ANTHROPIC_API_KEY no configurada")
        print("="*70)
        print("\nPara ejecutar este demo:")
        print("1. Crea archivo .env en la raíz del proyecto")
        print("2. Agrega: ANTHROPIC_API_KEY=tu_api_key_aqui")
        print("3. Vuelve a ejecutar este script")
        print("\nObtén tu API key en: https://console.anthropic.com/")
        return

    print("\n" + "="*70)
    print("CHOCHMAH (SABIDURÍA) - DEMOS")
    print("Razonamiento Profundo con Claude API")
    print("="*70)

    # Menú
    print("\nSelecciona demo:")
    print("1. Consulta Básica")
    print("2. Integración Keter → Chochmah")
    print("3. Humildad Epistémica")
    print("4. Configuración de Modelos")
    print("5. Métricas de Desempeño")
    print("6. Ejecutar TODAS las demos")
    print("0. Salir")

    choice = input("\nOpción: ").strip()

    demos = {
        '1': demo_basic_query,
        '2': demo_keter_chochmah_integration,
        '3': demo_epistemic_humility,
        '4': demo_model_configuration,
        '5': demo_metrics
    }

    if choice == '6':
        for demo_func in demos.values():
            try:
                demo_func()
                print("\n" + "-"*70)
            except Exception as e:
                print(f"\nError en demo: {e}")
                logger.exception("Error en demo")
    elif choice in demos:
        try:
            demos[choice]()
        except Exception as e:
            print(f"\nError: {e}")
            logger.exception("Error en demo")
    elif choice == '0':
        print("\n¡Hasta luego!")
    else:
        print("\nOpción inválida")


if __name__ == '__main__':
    main()
