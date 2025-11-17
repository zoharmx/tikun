"""
Test basico para Binah (Entendimiento)
Verifica que la Sefira de analisis contextual funciona correctamente.
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


def test_binah_basic():
    """Test basico de Binah"""
    print("=" * 70)
    print("TEST: Binah - Analisis Contextual Basico")
    print("=" * 70)

    # Crear instancia de Binah
    binah = Binah()

    # Input de prueba (simulando output de Chochmah)
    test_input = {
        'insights': """
        La implementacion de un sistema de credito social digital podria:
        1. Mejorar el cumplimiento de normas sociales
        2. Reducir comportamientos antisociales
        3. Optimizar asignacion de recursos basada en merito
        """,
        'analysis': """
        Este tipo de sistema utiliza datos comportamentales para asignar
        puntuaciones que determinan acceso a servicios y oportunidades.
        """,
        'query': 'Deberiamos implementar un sistema de credito social digital?'
    }

    print("\nINPUT (simulando Chochmah):")
    print(f"Query: {test_input['query']}")
    print(f"Insights: {test_input['insights'][:100]}...")

    print("\nLlamando a Binah.process()...")
    result = binah.process(test_input)

    if not result.get('processing_successful'):
        print(f"\nERROR: {result.get('error')}")
        return False

    print("\n" + "=" * 70)
    print("RESULTADO DE BINAH:")
    print("=" * 70)

    # Mostrar secciones
    sections = [
        'historical_context',
        'current_context',
        'stakeholders',
        'first_order_effects',
        'second_order_effects',
        'third_order_effects',
        'systemic_risks',
        'ethical_considerations',
        'contextual_synthesis'
    ]

    for section in sections:
        content = result.get(section, '')
        if content:
            print(f"\n{section.upper().replace('_', ' ')}:")
            print("-" * 70)
            print(content[:300] + "..." if len(content) > 300 else content)

    print(f"\n\nPERSPECTIVAS CONSIDERADAS: {result.get('perspectives_count', 0)}")

    # Validar alineamiento
    print("\n" + "=" * 70)
    print("VALIDACION DE ALINEAMIENTO:")
    print("=" * 70)

    alignment = binah.validate_alignment()
    print(f"Esta alineada: {alignment['is_aligned']}")
    print(f"Status: {alignment['status']}")
    print(f"Depth Score: {alignment.get('contextual_depth_score', 0):.2f}")
    print(f"Perspectivas promedio: {alignment.get('average_perspectives_per_activation', 0):.2f}")

    return True


def test_binah_with_chochmah():
    """Test de Binah recibiendo output real de Chochmah"""
    print("\n\n" + "=" * 70)
    print("TEST: Binah + Chochmah Integration")
    print("=" * 70)

    # Crear instancias
    chochmah = ChochmahGemini()
    binah = Binah()

    # Query de prueba
    query = """
    Una empresa de tecnologia quiere implementar un sistema de IA que
    automatice decisiones de contratacion para reducir sesgos humanos.
    Es esto etico y beneficioso?
    """

    print(f"\nQUERY: {query.strip()}")

    # Paso 1: Chochmah razona
    print("\nPASO 1: Chochmah razona...")
    chochmah_result = chochmah.process({'query': query})

    if not chochmah_result.get('processing_successful'):
        print(f"ERROR en Chochmah: {chochmah_result.get('error')}")
        return False

    print(f"Chochmah - Confidence: {chochmah_result.get('confidence_level', 0):.2f}")
    print(f"Insights: {chochmah_result.get('insights', '')[:150]}...")

    # Paso 2: Binah analiza contexto
    print("\nPASO 2: Binah analiza contexto...")
    binah_result = binah.process({
        'chochmah_output': chochmah_result,
        'query': query
    })

    if not binah_result.get('processing_successful'):
        print(f"ERROR en Binah: {binah_result.get('error')}")
        return False

    print("\n" + "=" * 70)
    print("ANALISIS CONTEXTUAL DE BINAH:")
    print("=" * 70)

    # Mostrar stakeholders y efectos de orden superior
    print("\nSTAKEHOLDERS:")
    print("-" * 70)
    print(binah_result.get('stakeholders', '')[:400])

    print("\n\nEFECTOS DE SEGUNDO ORDEN:")
    print("-" * 70)
    print(binah_result.get('second_order_effects', '')[:400])

    print("\n\nRIESGOS SISTEMICOS:")
    print("-" * 70)
    print(binah_result.get('systemic_risks', '')[:400])

    print(f"\n\nPERSPECTIVAS CONSIDERADAS: {binah_result.get('perspectives_count', 0)}")

    return True


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("SUITE DE TESTS PARA BINAH")
    print("=" * 70)

    # Test 1: Basico
    success1 = test_binah_basic()

    # Test 2: Integracion con Chochmah
    success2 = test_binah_with_chochmah()

    print("\n\n" + "=" * 70)
    print("RESUMEN DE TESTS")
    print("=" * 70)
    print(f"Test Basico: {'PASS' if success1 else 'FAIL'}")
    print(f"Test Integracion: {'PASS' if success2 else 'FAIL'}")

    if success1 and success2:
        print("\n>>> TODOS LOS TESTS PASARON <<<")
    else:
        print("\n>>> ALGUNOS TESTS FALLARON <<<")
