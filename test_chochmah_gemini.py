"""
Test de Chochmah con Gemini API
"""

import sys
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Agregar path del proyecto
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from src.sefirot.chochmah_gemini import ChochmahGemini

def test_chochmah_gemini():
    print("="*70)
    print("PRUEBA DE CHOCHMAH CON GEMINI API")
    print("="*70)

    # Inicializar ChochmahGemini
    print("\n1. Inicializando ChochmahGemini...")
    chochmah = ChochmahGemini()
    print(f"   Chochmah inicializada: {chochmah.name}")
    print(f"   Modelo: {chochmah.model_name}")
    print(f"   Cliente configurado: {'Si' if chochmah.client else 'No'}")

    # Consulta simple sobre Tikun Olam
    print("\n2. Procesando consulta sobre Tikun Olam...")
    query = {
        'query': '''Que es Tikun Olam y como puede la inteligencia artificial
        contribuir a este objetivo de reparacion y elevacion del mundo?''',
        'context': '''Estamos en 2025, desarrollando un sistema de IA basado en
        las 10 Sefirot del Arbol de la Vida cabalistico. El objetivo es crear
        IAG alineada antes del punto de inflexion predicho para 2029-2030.''',
        'objective': 'Maximizar Tikun Olam - florecimiento de toda la creacion'
    }

    print(f"   Query: {query['query'][:80]}...")

    result = chochmah.process(query)

    if result['processing_successful']:
        print("\n" + "="*70)
        print("RESULTADOS EXITOSOS")
        print("="*70)

        print(f"\n{'='*70}")
        print("COMPRENSION:")
        print(f"{'='*70}")
        print(result['understanding'])

        print(f"\n{'='*70}")
        print("ANALISIS:")
        print(f"{'='*70}")
        print(result['analysis'])

        print(f"\n{'='*70}")
        print("INSIGHTS CLAVE:")
        print(f"{'='*70}")
        print(result['insights'])

        print(f"\n{'='*70}")
        print("INCERTIDUMBRES RECONOCIDAS:")
        print(f"{'='*70}")
        print(result['uncertainties'])

        print(f"\n{'='*70}")
        print("RECOMENDACION:")
        print(f"{'='*70}")
        print(result['recommendation'])

        print(f"\n{'='*70}")
        print(f"NIVEL DE CONFIANZA: {result['confidence_level']:.2%}")
        print(f"{'='*70}")

        # Metricas
        print("\n" + "="*70)
        print("METRICAS DE DESEMPENO")
        print("="*70)
        metrics = chochmah.get_metrics()
        print(f"Sefira: {metrics['sefira']}")
        print(f"Posicion: {metrics['position']}")
        print(f"Activaciones: {metrics['activations']}")
        print(f"Tiempo total: {metrics['total_processing_time']:.2f}s")
        print(f"Tiempo promedio: {metrics['average_processing_time']:.2f}s")
        print(f"Tasa de exito: {metrics['success_rate']:.2%}")

        # Validacion de alineamiento
        print("\n" + "="*70)
        print("VALIDACION DE ALINEAMIENTO")
        print("="*70)
        validation = chochmah.validate_alignment()
        print(f"Alineada: {'SI' if validation['is_aligned'] else 'NO'}")
        print(f"Total activaciones: {validation['total_activations']}")
        print(f"Reconocimientos de incertidumbre: {validation['uncertainty_acknowledgments']}")
        print(f"Respuestas de alta confianza: {validation['high_confidence_responses']}")
        print(f"Ratio de humildad epistemica: {validation['epistemic_humility_ratio']:.2%}")
        print(f"Status: {validation['status']}")

        print("\n" + "="*70)
        print("PRUEBA EXITOSA - CHOCHMAH CON GEMINI FUNCIONA CORRECTAMENTE")
        print("="*70)

        return True

    else:
        print("\n" + "="*70)
        print("ERROR EN PROCESAMIENTO")
        print("="*70)
        print(f"Tipo de error: {result['error_type']}")
        print(f"Error: {result['error']}")
        return False

if __name__ == '__main__':
    success = test_chochmah_gemini()
    sys.exit(0 if success else 1)
