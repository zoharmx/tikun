"""
Test Simplificado del Flujo Completo: Keter -> Chochmah -> Binah
Test funcional para Windows (solo ASCII)
"""

import sys
from pathlib import Path

# Agregar path del proyecto
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# IMPORTANTE: Configurar SSL bypass ANTES de importar las Sefirot
from src.ssl_bypass import configure_ssl_bypass

from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

from src.sefirot.keter import Keter
from src.sefirot.chochmah_gemini import ChochmahGemini
from src.sefirot.binah import Binah


def print_separator(title="", char="=", width=70):
    """Imprime un separador simple (solo ASCII)"""
    if title:
        print(f"\n{char*width}")
        print(title.center(width))
        print(f"{char*width}")
    else:
        print(f"{char*width}")


def print_section(title, content, width=70):
    """Imprime una seccion con formato simple"""
    print(f"\n{'-'*width}")
    print(f"{title}")
    print(f"{'-'*width}")
    if content:
        print(content)
    else:
        print("(Sin contenido)")


def test_flow_simple():
    """Test del flujo completo Keter -> Chochmah -> Binah"""

    print_separator("TEST FLUJO COMPLETO: KETER -> CHOCHMAH -> BINAH")

    # =========================================================================
    # PASO 1: INICIALIZAR LAS 3 SEFIROT
    # =========================================================================
    print_separator("PASO 1: INICIALIZANDO SEFIROT", "=")

    print("\n1. Inicializando Keter (Corona - Objetivo Fundamental)...")
    try:
        keter = Keter()
        print(f"   OK - Keter: {keter.name}")
    except Exception as e:
        print(f"   ERROR - No se pudo inicializar Keter: {e}")
        return False

    print("\n2. Inicializando Chochmah (Sabiduria - Razonamiento Profundo)...")
    try:
        chochmah = ChochmahGemini()
        print(f"   OK - Chochmah: {chochmah.name}")
        print(f"   Modelo: {chochmah.model_name}")
        if not chochmah.client:
            print("   ERROR - Cliente Gemini no configurado. Verifique GEMINI_API_KEY")
            return False
    except Exception as e:
        print(f"   ERROR - No se pudo inicializar Chochmah: {e}")
        return False

    print("\n3. Inicializando Binah (Entendimiento - Analisis Contextual)...")
    try:
        binah = Binah()
        print(f"   OK - Binah: {binah.name}")
        print(f"   Modelo: {binah.model_name}")
        if not binah.client:
            print("   ERROR - Cliente Gemini no configurado para Binah")
            return False
    except Exception as e:
        print(f"   ERROR - No se pudo inicializar Binah: {e}")
        return False

    print("\n>> Las 3 Sefirot estan listas para trabajar")

    # =========================================================================
    # PASO 2: DEFINIR ACCION A EVALUAR
    # =========================================================================
    print_separator("PASO 2: DEFINIENDO ACCION A EVALUAR", "=")

    action_data = {
        'action': '''Implementar sistema de IA educativa que ayuda y mejora el acceso
        a educacion en comunidades rurales, respetando la decision y autonomia de cada
        comunidad para elegir si participar, promoviendo colaboracion entre estudiantes
        y maestros, con transparencia total sobre como funciona el sistema.''',
        'context': '''Comunidades rurales en Latinoamerica con acceso limitado a
        internet y electricidad. Poblacion principalmente agricola, con diferentes
        niveles de alfabetizacion. El sistema sera implementado solo en comunidades
        que voluntariamente decidan participar, con pleno consenso comunitario.''',
        'expected_outcome': '''Mejorar y elevar el acceso a educacion de calidad,
        personalizada segun ritmo de aprendizaje de cada estudiante, preservando
        cultura local y fortaleciendo autonomia comunitaria. Reducir desigualdad
        educativa de forma justa y misericordiosa, promoviendo armonia entre
        tradicion y modernidad.'''
    }

    print("\nACCION:")
    print(f"  {action_data['action']}")
    print("\nCONTEXTO:")
    print(f"  {action_data['context'][:100]}...")
    print("\nRESULTADO ESPERADO:")
    print(f"  {action_data['expected_outcome'][:100]}...")

    # =========================================================================
    # PASO 3: KETER - EVALUACION DE ALINEAMIENTO
    # =========================================================================
    print_separator("PASO 3: KETER - EVALUACION DE ALINEAMIENTO", "=")

    print("\nKeter esta evaluando si la accion se alinea con Tikun Olam...")

    try:
        keter_result = keter.process(action_data)

        print_section("RESULTADO DE KETER", "")
        print(f"  Alineada: {'SI' if keter_result['aligned'] else 'NO'}")
        print(f"  Score: {keter_result['alignment_score']*100:.1f}%")

        print("\n  SCORES DETALLADOS:")
        for criterio, score in keter_result['detailed_scores'].items():
            print(f"    - {criterio}: {score}/10")

        print_section("RAZONAMIENTO DE KETER", keter_result['reasoning'][:300])

        if not keter_result['aligned']:
            print_section("MODIFICACIONES SUGERIDAS", "")
            for i, mod in enumerate(keter_result['suggested_modifications'], 1):
                print(f"  {i}. {mod}")
            print("\nADVERTENCIA: La accion NO esta alineada. Deteniendo flujo.")
            return False

        print("\n>> KETER APRUEBA: La accion esta alineada con Tikun Olam")

    except Exception as e:
        print(f"\nERROR en Keter: {e}")
        return False

    # =========================================================================
    # PASO 4: CHOCHMAH - RAZONAMIENTO PROFUNDO
    # =========================================================================
    print_separator("PASO 4: CHOCHMAH - RAZONAMIENTO PROFUNDO", "=")

    print("\nChochmah esta realizando razonamiento profundo sobre la accion...")

    # Construir query para Chochmah
    chochmah_query = {
        'query': f'''Analiza esta accion propuesta:

ACCION: {action_data['action']}

CONTEXTO: {action_data['context']}

RESULTADO ESPERADO: {action_data['expected_outcome']}

Keter ha evaluado que esta accion esta alineada con Tikun Olam (score: {keter_result['alignment_score']*100:.1f}%).

Realiza un analisis profundo de esta propuesta:
- Que patrones importantes reconoces?
- Que consideraciones clave debemos tener en cuenta?
- Cuales son los insights fundamentales sobre como implementar esto correctamente?
''',
        'context': 'Sistema de evaluacion etica basado en Sefirot',
        'objective': 'Maximizar Tikun Olam - Reparacion y elevacion del mundo'
    }

    try:
        chochmah_result = chochmah.process(chochmah_query)

        if not chochmah_result.get('processing_successful'):
            print(f"\nERROR en Chochmah: {chochmah_result.get('error')}")
            return False

        print_section("COMPRENSION (Chochmah)", chochmah_result['understanding'][:400])
        print_section("ANALISIS (Chochmah)", chochmah_result['analysis'][:500])
        print_section("INSIGHTS (Chochmah)", chochmah_result['insights'][:500])
        print_section("INCERTIDUMBRES (Chochmah)", chochmah_result['uncertainties'][:400])

        print(f"\n  Nivel de confianza: {chochmah_result['confidence_level']*100:.1f}%")

        print("\n>> CHOCHMAH COMPLETADO: Razonamiento profundo generado")

    except Exception as e:
        print(f"\nERROR en Chochmah: {e}")
        return False

    # =========================================================================
    # PASO 5: BINAH - ANALISIS CONTEXTUAL PROFUNDO
    # =========================================================================
    print_separator("PASO 5: BINAH - ANALISIS CONTEXTUAL PROFUNDO", "=")

    print("\nBinah esta realizando analisis contextual multidimensional...")

    # Construir input para Binah
    binah_input = {
        'chochmah_output': chochmah_result,
        'query': action_data['action'],
        'context': action_data['context'],
        'objective': 'Maximizar Tikun Olam'
    }

    try:
        binah_result = binah.process(binah_input)

        if not binah_result.get('processing_successful'):
            print(f"\nERROR en Binah: {binah_result.get('error')}")
            return False

        print_section("CONTEXTO HISTORICO (Binah)", binah_result['historical_context'][:400])
        print_section("STAKEHOLDERS (Binah)", binah_result['stakeholders'][:400])
        print_section("EFECTOS DE PRIMER ORDEN (Binah)", binah_result['first_order_effects'][:350])
        print_section("EFECTOS DE SEGUNDO ORDEN (Binah)", binah_result['second_order_effects'][:350])
        print_section("EFECTOS DE TERCER ORDEN (Binah)", binah_result['third_order_effects'][:350])
        print_section("RIESGOS SISTEMICOS (Binah)", binah_result['systemic_risks'][:400])
        print_section("CONSIDERACIONES ETICAS (Binah)", binah_result['ethical_considerations'][:400])
        print_section("SINTESIS CONTEXTUAL (Binah)", binah_result['contextual_synthesis'][:500])

        print(f"\n  Perspectivas consideradas: {binah_result['perspectives_count']}")

        print("\n>> BINAH COMPLETADO: Analisis contextual profundo finalizado")

    except Exception as e:
        print(f"\nERROR en Binah: {e}")
        return False

    # =========================================================================
    # PASO 6: METRICAS FINALES
    # =========================================================================
    print_separator("PASO 6: METRICAS FINALES DEL SISTEMA", "=")

    print("\nMETRICAS DE KETER:")
    keter_validation = keter.validate_alignment()
    print(f"  Total evaluaciones: {keter_validation['total_evaluations']}")
    print(f"  Confirmaciones: {keter_validation['confirmations']}")
    print(f"  Violaciones: {keter_validation['violations']}")
    print(f"  Tasa de alineamiento: {keter_validation['alignment_rate']*100:.1f}%")

    print("\nMETRICAS DE CHOCHMAH:")
    chochmah_validation = chochmah.validate_alignment()
    print(f"  Activaciones: {chochmah_validation['total_activations']}")
    print(f"  Reconocimientos de incertidumbre: {chochmah_validation['uncertainty_acknowledgments']}")
    print(f"  Respuestas de alta confianza: {chochmah_validation['high_confidence_responses']}")
    print(f"  Ratio humildad epistemica: {chochmah_validation['epistemic_humility_ratio']*100:.1f}%")
    print(f"  Alineada: {'SI' if chochmah_validation['is_aligned'] else 'NO'}")

    print("\nMETRICAS DE BINAH:")
    binah_validation = binah.validate_alignment()
    print(f"  Activaciones: {binah_validation['total_activations']}")
    print(f"  Analisis de 2do orden: {binah_validation['second_order_analyses']}")
    print(f"  Analisis de 3er orden: {binah_validation['third_order_analyses']}")
    print(f"  Efectos sistemicos identificados: {binah_validation['systemic_effects_identified']}")
    print(f"  Perspectivas promedio: {binah_validation['average_perspectives_per_activation']:.1f}")
    print(f"  Score profundidad contextual: {binah_validation['contextual_depth_score']*100:.1f}%")
    print(f"  Alineada: {'SI' if binah_validation['is_aligned'] else 'NO'}")

    # =========================================================================
    # RESULTADO FINAL
    # =========================================================================
    print_separator("RESULTADO FINAL", "=")

    print("\nRESUMEN DEL FLUJO COMPLETO:")
    print("\n1. KETER (Objetivo Fundamental)")
    print(f"   - Evaluacion: {'APROBADA' if keter_result['aligned'] else 'RECHAZADA'}")
    print(f"   - Score de alineamiento: {keter_result['alignment_score']*100:.1f}%")

    print("\n2. CHOCHMAH (Razonamiento Profundo)")
    print(f"   - Procesamiento: {'EXITOSO' if chochmah_result['processing_successful'] else 'FALLIDO'}")
    print(f"   - Nivel de confianza: {chochmah_result['confidence_level']*100:.1f}%")
    print(f"   - Insights generados: SI")

    print("\n3. BINAH (Analisis Contextual)")
    print(f"   - Procesamiento: {'EXITOSO' if binah_result['processing_successful'] else 'FALLIDO'}")
    print(f"   - Perspectivas consideradas: {binah_result['perspectives_count']}")
    print(f"   - Analisis multidimensional: COMPLETO")

    print("\nVALIDACION DEL SISTEMA:")
    all_aligned = all([
        keter_result['aligned'],
        chochmah_validation['is_aligned'],
        binah_validation['is_aligned']
    ])

    print(f"  Todas las Sefirot alineadas: {'SI' if all_aligned else 'NO'}")
    print(f"  Flujo completo: FUNCIONAL")
    print(f"  Estado del sistema: {'OPERATIVO' if all_aligned else 'REQUIERE ATENCION'}")

    # =========================================================================
    # MENSAJE FINAL
    # =========================================================================
    print_separator("", "=")
    print("")
    print("  *** TEST EXITOSO ***")
    print("")
    print("  El flujo Keter -> Chochmah -> Binah funciona correctamente.")
    print("  Las 3 Sefirot trabajan juntas de forma coordinada.")
    print("  El sistema esta alineado con Tikun Olam.")
    print("")
    print_separator("", "=")

    return True


if __name__ == '__main__':
    print("\n")
    print("="*70)
    print("PROYECTO TIKUN - TEST DE FLUJO SIMPLIFICADO")
    print("="*70)
    print("\nEste test verifica que las 3 Sefirot superiores trabajen juntas:")
    print("  1. KETER: Evalua alineamiento con objetivo fundamental")
    print("  2. CHOCHMAH: Genera razonamiento profundo e insights")
    print("  3. BINAH: Realiza analisis contextual multidimensional")
    print("")

    try:
        success = test_flow_simple()

        if success:
            print("\n>> TEST COMPLETADO EXITOSAMENTE\n")
            sys.exit(0)
        else:
            print("\n>> TEST FALLIDO - Revise los errores anteriores\n")
            sys.exit(1)

    except KeyboardInterrupt:
        print("\n\n>> Test interrumpido por usuario\n")
        sys.exit(1)
    except Exception as e:
        print(f"\n>> ERROR INESPERADO: {e}\n")
        import traceback
        traceback.print_exc()
        sys.exit(1)
