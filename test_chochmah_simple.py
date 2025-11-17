"""
Test simple de Chochmah con API real de Anthropic Claude
"""

import sys
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Agregar path del proyecto
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from src.sefirot.chochmah import Chochmah

def test_chochmah():
    print("="*70)
    print("PRUEBA DE CHOCHMAH - RAZONAMIENTO PROFUNDO CON CLAUDE")
    print("="*70)

    # Inicializar Chochmah
    print("\n1. Inicializando Chochmah...")
    chochmah = Chochmah()
    print(f"   Chochmah inicializada: {chochmah.name}")
    print(f"   Modelo: {chochmah.model}")
    print(f"   Cliente configurado: {'Si' if chochmah.client else 'No'}")

    # Consulta simple
    print("\n2. Procesando consulta de prueba...")
    query = {
        'query': 'Que es Tikun Olam y como puede la IA contribuir a este objetivo?',
        'context': 'Estamos desarrollando un sistema de IA alineado con principios de reparacion del mundo',
        'objective': 'Maximizar Tikun Olam'
    }

    print(f"   Query: {query['query']}")

    result = chochmah.process(query)

    if result['processing_successful']:
        print("\n" + "="*70)
        print("RESULTADOS")
        print("="*70)

        print(f"\n[COMPRENSION]")
        print(result['understanding'][:300] + "..." if len(result['understanding']) > 300 else result['understanding'])

        print(f"\n[ANALISIS]")
        print(result['analysis'][:300] + "..." if len(result['analysis']) > 300 else result['analysis'])

        print(f"\n[INSIGHTS]")
        print(result['insights'][:300] + "..." if len(result['insights']) > 300 else result['insights'])

        print(f"\n[INCERTIDUMBRES]")
        print(result['uncertainties'][:300] + "..." if len(result['uncertainties']) > 300 else result['uncertainties'])

        print(f"\n[RECOMENDACION]")
        print(result['recommendation'][:300] + "..." if len(result['recommendation']) > 300 else result['recommendation'])

        print(f"\n[CONFIANZA]: {result['confidence_level']:.2f}")

        # Metricas
        print("\n" + "="*70)
        print("METRICAS")
        print("="*70)
        metrics = chochmah.get_metrics()
        print(f"Activaciones: {metrics['activations']}")
        print(f"Tiempo de procesamiento: {metrics['total_processing_time']:.2f}s")
        print(f"Tasa de exito: {metrics['success_rate']:.2%}")

        # Validacion de alineamiento
        print("\n" + "="*70)
        print("VALIDACION DE ALINEAMIENTO")
        print("="*70)
        validation = chochmah.validate_alignment()
        print(f"Alineada: {validation['is_aligned']}")
        print(f"Ratio de humildad epistemica: {validation['epistemic_humility_ratio']:.2f}")
        print(f"Status: {validation['status']}")

        print("\n" + "="*70)
        print("PRUEBA EXITOSA!")
        print("="*70)

    else:
        print("\n" + "="*70)
        print("ERROR EN PROCESAMIENTO")
        print("="*70)
        print(f"Tipo de error: {result['error_type']}")
        print(f"Error: {result['error']}")

if __name__ == '__main__':
    test_chochmah()
