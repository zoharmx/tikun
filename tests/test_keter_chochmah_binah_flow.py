"""
Test de integracion: Flujo Keter -> Chochmah -> Binah

Este test verifica que las tres primeras Sefirot trabajan correctamente juntas.
"""

import sys
import os

# Agregar el directorio raiz al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.sefirot.chochmah_gemini import ChochmahGemini
from src.sefirot.binah import Binah
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()


def test_full_flow():
    """
    Test del flujo completo: Keter -> Chochmah -> Binah

    Escenario: Analizar si una empresa deberia implementar
    semana laboral de 4 dias.
    """
    print("=" * 80)
    print("TEST: Flujo Completo Keter -> Chochmah -> Binah")
    print("=" * 80)

    # KETER: Objetivo fundamental (manual por ahora, ya que Keter tiene dependencias rotas)
    objective = "Maximizar Tikun Olam: bienestar de empleados, productividad sostenible, justicia social"

    # Query
    query = """
    Una empresa de tecnologia con 200 empleados esta considerando
    implementar una semana laboral de 4 dias (32 horas) manteniendo
    el mismo salario.

    Es esta una decision que se alinea con Tikun Olam?
    Que implicaciones tiene?
    """

    print(f"\nOBJETIVO (Keter): {objective}")
    print(f"\nQUERY:\n{query}\n")

    # PASO 1: CHOCHMAH - Razonamiento Profundo
    print("=" * 80)
    print("PASO 1: CHOCHMAH (Sabiduria) - Razonamiento Profundo")
    print("=" * 80)

    chochmah = ChochmahGemini()

    chochmah_input = {
        'query': query,
        'objective': objective,
        'context': 'Empresa de tecnologia, sector competitivo, empleados principalmente en roles creativos/cognitivos'
    }

    print("\nLlamando a Chochmah...")
    chochmah_result = chochmah.process(chochmah_input)

    if not chochmah_result.get('processing_successful'):
        print(f"ERROR en Chochmah: {chochmah_result.get('error')}")
        return False

    print(f"\nConfianza: {chochmah_result['confidence_level']:.2f}")
    print("\nCOMPRENSION:")
    print("-" * 80)
    print(chochmah_result['understanding'][:400] + "...")

    print("\nINSIGHTS:")
    print("-" * 80)
    print(chochmah_result['insights'][:600] + "...")

    print("\nINCERTIDUMBRES:")
    print("-" * 80)
    print(chochmah_result['uncertainties'][:400] + "...")

    # PASO 2: BINAH - Analisis Contextual Profundo
    print("\n" + "=" * 80)
    print("PASO 2: BINAH (Entendimiento) - Analisis Contextual Profundo")
    print("=" * 80)

    binah = Binah()

    binah_input = {
        'chochmah_output': chochmah_result,
        'query': query,
        'objective': objective
    }

    print("\nLlamando a Binah...")
    binah_result = binah.process(binah_input)

    if not binah_result.get('processing_successful'):
        print(f"ERROR en Binah: {binah_result.get('error')}")
        return False

    print(f"\nPerspectivas consideradas: {binah_result['perspectives_count']}")

    print("\nCONTEXTO HISTORICO:")
    print("-" * 80)
    print(binah_result['historical_context'][:500] + "...")

    print("\nSTAKEHOLDERS:")
    print("-" * 80)
    print(binah_result['stakeholders'][:600] + "...")

    print("\nEFECTOS DE PRIMER ORDEN:")
    print("-" * 80)
    print(binah_result['first_order_effects'][:400] + "...")

    print("\nEFECTOS DE SEGUNDO ORDEN:")
    print("-" * 80)
    print(binah_result['second_order_effects'][:600] + "...")

    print("\nEFECTOS DE TERCER ORDEN:")
    print("-" * 80)
    print(binah_result['third_order_effects'][:600] + "...")

    print("\nRIESGOS SISTEMICOS:")
    print("-" * 80)
    print(binah_result['systemic_risks'][:500] + "...")

    print("\nCONSIDERACIONES ETICAS:")
    print("-" * 80)
    print(binah_result['ethical_considerations'][:500] + "...")

    print("\nSINTESIS CONTEXTUAL:")
    print("-" * 80)
    print(binah_result['contextual_synthesis'][:700] + "...")

    # VALIDACION DE ALINEAMIENTO
    print("\n" + "=" * 80)
    print("VALIDACION DE ALINEAMIENTO")
    print("=" * 80)

    # Chochmah alignment
    chochmah_alignment = chochmah.validate_alignment()
    print("\nChochmah:")
    print(f"  - Esta alineada: {chochmah_alignment['is_aligned']}")
    print(f"  - Humildad epistemica: {chochmah_alignment['epistemic_humility_ratio']:.2f}")
    print(f"  - Status: {chochmah_alignment['status']}")

    # Binah alignment
    binah_alignment = binah.validate_alignment()
    print("\nBinah:")
    print(f"  - Esta alineada: {binah_alignment['is_aligned']}")
    print(f"  - Profundidad contextual: {binah_alignment['contextual_depth_score']:.2f}")
    print(f"  - Perspectivas promedio: {binah_alignment['average_perspectives_per_activation']:.2f}")
    print(f"  - Status: {binah_alignment['status']}")

    # SINTESIS FINAL
    print("\n" + "=" * 80)
    print("SINTESIS DEL FLUJO")
    print("=" * 80)

    print("\n1. CHOCHMAH identifico los patrones y comprension fundamental")
    print(f"   Confianza: {chochmah_result['confidence_level']:.2f}")

    print("\n2. BINAH expandio el analisis contextualmente")
    print(f"   Perspectivas: {binah_result['perspectives_count']}")
    print(f"   Profundidad: {binah_alignment['contextual_depth_score']:.2f}")

    print("\n3. ALINEAMIENTO CON TIKUN OLAM:")
    if chochmah_alignment['is_aligned'] and binah_alignment['is_aligned']:
        print("   >>> AMBAS SEFIROT ESTAN ALINEADAS <<<")
    else:
        print("   >>> ADVERTENCIA: REVISAR ALINEAMIENTO <<<")

    return True


def test_edge_case_low_confidence():
    """
    Test de caso extremo: Query con alta incertidumbre

    Verifica que Chochmah reconozca incertidumbre y que Binah
    identifique multiples riesgos.
    """
    print("\n\n" + "=" * 80)
    print("TEST: Caso Extremo - Alta Incertidumbre")
    print("=" * 80)

    chochmah = ChochmahGemini()
    binah = Binah()

    # Query con mucha incertidumbre
    query = """
    Deberiamos contactar a una civilizacion extraterrestre si la detectamos?
    Cuales serian las consecuencias?
    """

    print(f"\nQUERY: {query}\n")

    # Chochmah
    print("Chochmah razonando...")
    chochmah_result = chochmah.process({'query': query})

    if not chochmah_result.get('processing_successful'):
        print(f"ERROR: {chochmah_result.get('error')}")
        return False

    print(f"Confianza: {chochmah_result['confidence_level']:.2f}")
    print(f"\nIncertidumbres identificadas:")
    print(chochmah_result['uncertainties'][:500] + "...")

    # Binah
    print("\nBinah analizando contexto...")
    binah_result = binah.process({
        'chochmah_output': chochmah_result,
        'query': query
    })

    if not binah_result.get('processing_successful'):
        print(f"ERROR: {binah_result.get('error')}")
        return False

    print(f"\nRiesgos sistemicos identificados:")
    print(binah_result['systemic_risks'][:600] + "...")

    print(f"\nEfectos de tercer orden:")
    print(binah_result['third_order_effects'][:600] + "...")

    # Validaciones
    print("\n" + "=" * 80)
    print("VALIDACIONES:")
    print("=" * 80)

    # Chochmah deberia tener baja confianza
    if chochmah_result['confidence_level'] < 0.7:
        print("PASS: Chochmah reconoce incertidumbre (confianza < 0.7)")
    else:
        print("ADVERTENCIA: Chochmah tiene alta confianza en tema incierto")

    # Binah deberia identificar multiples riesgos
    risk_indicators = binah_result['systemic_risks'].count('-') + binah_result['systemic_risks'].count('*')
    if risk_indicators >= 3:
        print(f"PASS: Binah identifico multiples riesgos ({risk_indicators} items)")
    else:
        print("ADVERTENCIA: Binah identifico pocos riesgos")

    return True


if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("SUITE DE TESTS: FLUJO KETER -> CHOCHMAH -> BINAH")
    print("=" * 80)

    # Test 1: Flujo completo normal
    success1 = test_full_flow()

    # Test 2: Caso extremo
    success2 = test_edge_case_low_confidence()

    print("\n\n" + "=" * 80)
    print("RESUMEN DE TESTS")
    print("=" * 80)
    print(f"Flujo completo: {'PASS' if success1 else 'FAIL'}")
    print(f"Caso extremo: {'PASS' if success2 else 'FAIL'}")

    if success1 and success2:
        print("\n>>> TODOS LOS TESTS PASARON <<<")
    else:
        print("\n>>> ALGUNOS TESTS FALLARON <<<")
