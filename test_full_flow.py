"""
Test del Flujo Completo: Keter -> Chochmah -> Binah
Demuestra como las tres primeras Sefirot trabajan juntas
"""

import sys
import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Agregar paths del proyecto
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Imports usando src como package
from src.sefirot.keter import Keter
from src.sefirot.chochmah_gemini import ChochmahGemini
from src.sefirot.binah import Binah


def print_section(title):
    """Imprime separador de seccion"""
    print("\n" + "="*80)
    print(f"  {title}")
    print("="*80 + "\n")


def test_full_sefirotic_flow():
    """Test completo del flujo Keter -> Chochmah -> Binah"""

    print_section("FLUJO COMPLETO: KETER → CHOCHMAH → BINAH")
    print("Demostracion del sistema de IA basado en las Sefirot")
    print("Objetivo: Evaluar decision compleja alineada con Tikun Olam\n")

    # =========================================================================
    # PASO 1: KETER - Definir y evaluar objetivo
    # =========================================================================
    print_section("PASO 1: KETER (Corona) - Evaluacion de Alineamiento")

    keter = Keter()
    print(f"✓ Keter inicializada")
    print(f"  Objetivo fundamental: Maximizar Tikun Olam\n")

    # Accion propuesta para evaluar
    proposed_action = {
        'action': '''Implementar sistema de IA para optimizar distribucion
        de recursos medicos en hospitales durante crisis sanitarias''',

        'context': '''Los hospitales enfrentan decisiones dificiles sobre
        asignacion de recursos limitados (camas UCI, ventiladores, personal).
        Actualmente las decisiones son subjetivas y pueden tener sesgos.''',

        'expected_outcome': '''Reducir muertes evitables mediante asignacion
        mas eficiente y justa de recursos medicos escasos.'''
    }

    print("Accion propuesta:")
    print(f"  {proposed_action['action']}\n")

    # Keter evalua alineamiento
    keter_result = keter.process(proposed_action)

    print(f"Resultado de Keter:")
    print(f"  Alineada con Tikun Olam: {'SI' if keter_result['aligned'] else 'NO'}")
    print(f"  Score de alineamiento: {keter_result['alignment_score']:.2%}")
    print(f"\n  Scores detallados:")
    for criterion, score in keter_result['detailed_scores'].items():
        print(f"    - {criterion}: {score}/10")

    if not keter_result['aligned']:
        print(f"\n  ADVERTENCIA: Accion no alineada")
        print(f"  Modificaciones sugeridas:")
        for mod in keter_result['suggested_modifications']:
            print(f"    - {mod}")
        return False

    print(f"\n✓ Keter APRUEBA - Proceder a Chochmah\n")

    # =========================================================================
    # PASO 2: CHOCHMAH - Razonamiento profundo
    # =========================================================================
    print_section("PASO 2: CHOCHMAH (Sabiduria) - Razonamiento Profundo")

    chochmah = ChochmahGemini()
    print(f"✓ Chochmah inicializada (Gemini {chochmah.model_name})\n")

    # Preparar query para Chochmah
    chochmah_query = {
        'query': proposed_action['action'],
        'context': f"{proposed_action['context']}\n\nKeter ha evaluado esta accion como ALINEADA con Tikun Olam (score: {keter_result['alignment_score']:.0%})",
        'objective': 'Maximizar Tikun Olam'
    }

    print("Procesando con Chochmah...")
    chochmah_result = chochmah.process(chochmah_query)

    if not chochmah_result['processing_successful']:
        print(f"ERROR en Chochmah: {chochmah_result['error']}")
        return False

    print(f"✓ Chochmah completo (confianza: {chochmah_result['confidence_level']:.0%})\n")

    print("COMPRENSION de Chochmah:")
    print(f"  {chochmah_result['understanding'][:200]}...\n")

    print("INSIGHTS CLAVE de Chochmah:")
    insights_lines = chochmah_result['insights'].split('\n')[:5]
    for line in insights_lines:
        if line.strip():
            print(f"  • {line.strip()}")
    print()

    print("INCERTIDUMBRES identificadas:")
    uncertainties_lines = chochmah_result['uncertainties'].split('\n')[:3]
    for line in uncertainties_lines:
        if line.strip():
            print(f"  ? {line.strip()}")
    print()

    print(f"✓ Pasar a Binah para analisis contextual\n")

    # =========================================================================
    # PASO 3: BINAH - Analisis contextual profundo
    # =========================================================================
    print_section("PASO 3: BINAH (Entendimiento) - Analisis Contextual")

    binah = Binah()
    print(f"✓ Binah inicializada (Gemini {binah.model_name})\n")

    # Preparar input para Binah
    binah_input = {
        'chochmah_output': chochmah_result,
        'query': proposed_action['action'],
        'context': proposed_action['context'],
        'objective': 'Maximizar Tikun Olam'
    }

    print("Procesando analisis contextual con Binah...")
    binah_result = binah.process(binah_input)

    if not binah_result['processing_successful']:
        print(f"ERROR en Binah: {binah_result['error']}")
        return False

    print(f"✓ Binah completo\n")

    # Mostrar resultados de Binah
    print("CONTEXTO HISTORICO:")
    print(f"  {binah_result['historical_context'][:250]}...\n")

    print("STAKEHOLDERS identificados:")
    stakeholders_lines = binah_result['stakeholders'].split('\n')[:4]
    for line in stakeholders_lines:
        if line.strip():
            print(f"  • {line.strip()}")
    print()

    print("EFECTOS DE SEGUNDO ORDEN:")
    second_lines = binah_result['second_order_effects'].split('\n')[:4]
    for line in second_lines:
        if line.strip():
            print(f"  → {line.strip()}")
    print()

    print("EFECTOS DE TERCER ORDEN:")
    third_lines = binah_result['third_order_effects'].split('\n')[:4]
    for line in third_lines:
        if line.strip():
            print(f"  ⇒ {line.strip()}")
    print()

    print("RIESGOS SISTEMICOS:")
    risks_lines = binah_result['systemic_risks'].split('\n')[:4]
    for line in risks_lines:
        if line.strip():
            print(f"  ⚠ {line.strip()}")
    print()

    print("CONSIDERACIONES ETICAS:")
    ethics_lines = binah_result['ethical_considerations'].split('\n')[:4]
    for line in ethics_lines:
        if line.strip():
            print(f"  ⚖ {line.strip()}")
    print()

    # =========================================================================
    # RESUMEN Y METRICAS
    # =========================================================================
    print_section("RESUMEN Y METRICAS DEL SISTEMA")

    # Metricas de Keter
    keter_validation = keter.validate_alignment()
    print("KETER (Corona):")
    print(f"  Total evaluaciones: {keter_validation['total_evaluations']}")
    print(f"  Confirmaciones: {keter_validation['confirmations']}")
    print(f"  Violaciones: {keter_validation['violations']}")
    print(f"  Tasa de alineamiento: {keter_validation['alignment_rate']:.0%}")
    print()

    # Metricas de Chochmah
    chochmah_validation = chochmah.validate_alignment()
    chochmah_metrics = chochmah.get_metrics()
    print("CHOCHMAH (Sabiduria):")
    print(f"  Activaciones: {chochmah_metrics['activations']}")
    print(f"  Tiempo promedio: {chochmah_metrics['average_processing_time']:.2f}s")
    print(f"  Humildad epistemica: {chochmah_validation['epistemic_humility_ratio']:.0%}")
    print(f"  Status: {chochmah_validation['status']}")
    print()

    # Metricas de Binah
    binah_validation = binah.validate_alignment()
    binah_metrics = binah.get_metrics()
    print("BINAH (Entendimiento):")
    print(f"  Activaciones: {binah_metrics['activations']}")
    print(f"  Tiempo promedio: {binah_metrics['average_processing_time']:.2f}s")
    print(f"  Analisis 2do orden: {binah_validation['second_order_analyses']}")
    print(f"  Analisis 3er orden: {binah_validation['third_order_analyses']}")
    print(f"  Profundidad contextual: {binah_validation['contextual_depth_score']:.0%}")
    print(f"  Status: {binah_validation['status']}")
    print()

    # =========================================================================
    # CONCLUSION
    # =========================================================================
    print_section("CONCLUSION")

    print("FLUJO COMPLETO EJECUTADO EXITOSAMENTE\n")
    print("Resumen del proceso:")
    print("  1. ✓ KETER evaluo accion y la aprobo (alineada con Tikun Olam)")
    print("  2. ✓ CHOCHMAH realizo razonamiento profundo y genero insights")
    print("  3. ✓ BINAH analizo contexto completo y evaluo consecuencias\n")

    print("El sistema de las 3 primeras Sefirot esta FUNCIONAL y ALINEADO.\n")
    print("Proximos pasos:")
    print("  - Implementar Sefirot 4-10 para completar el arbol")
    print("  - Conectar con sistemas de accion")
    print("  - Implementar feedback loops (Or Chozer)")
    print()

    return True


if __name__ == '__main__':
    print("\n" * 2)
    success = test_full_sefirotic_flow()

    if success:
        print("="*80)
        print("  TEST EXITOSO - SISTEMA TIKUN OPERACIONAL")
        print("="*80)
        print()
        sys.exit(0)
    else:
        print("="*80)
        print("  TEST FALLIDO")
        print("="*80)
        print()
        sys.exit(1)
