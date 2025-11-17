"""
Test basico de Chesed (Misericordia/Bondad)
Verifica que la Sefira identifica oportunidades de dar y reconoce limites
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.sefirot.chesed import Chesed
from src.sefirot.binah import Binah
from src.sefirot.chochmah_gemini import ChochmahGemini
from src.sefirot.keter import Keter
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()


def test_chesed_basic():
    """Test basico del flujo completo hasta Chesed"""

    print("\n" + "="*80)
    print("TEST BASICO CHESED - Sistema Tikun Olam")
    print("="*80)

    # 1. KETER - Define objetivo
    print("\n[1/4] KETER - Evaluando alineamiento con Tikun Olam...")
    keter = Keter(use_llm_scoring=True)

    action_input = {
        'action': 'Implementar sistema de IA educativa en comunidades rurales',
        'context': 'Comunidades con acceso limitado a educacion de calidad',
        'expected_outcome': 'Mejorar alfabetizacion digital y acceso a conocimiento'
    }

    keter_result = keter.process(action_input)

    print(f"  Alineamiento: {keter_result['aligned']}")
    print(f"  Score: {keter_result['alignment_score']*100:.1f}%")

    if not keter_result['aligned']:
        print("\n>> KETER RECHAZA LA ACCION - No proceder")
        return

    # 2. CHOCHMAH - Razonamiento profundo
    print("\n[2/4] CHOCHMAH - Razonamiento profundo...")
    chochmah = ChochmahGemini()

    chochmah_input = {
        'query': action_input['action'],
        'context': action_input['context'],
        'objective': 'Maximizar Tikun Olam'
    }

    chochmah_result = chochmah.process(chochmah_input)

    if not chochmah_result.get('processing_successful'):
        print(f"  ERROR en Chochmah: {chochmah_result.get('error')}")
        return

    print(f"  Confianza: {chochmah_result['confidence_level']*100:.1f}%")
    print(f"  Incertidumbres reconocidas: {'Si' if len(chochmah_result['uncertainties']) > 30 else 'No'}")

    # 3. BINAH - Analisis contextual
    print("\n[3/4] BINAH - Analisis contextual...")
    binah = Binah()

    binah_input = {
        'understanding': chochmah_result['understanding'],
        'analysis': chochmah_result['analysis'],
        'action': action_input['action']
    }

    binah_result = binah.process(binah_input)

    if not binah_result.get('processing_successful'):
        print(f"  ERROR en Binah: {binah_result.get('error')}")
        return

    print(f"  Perspectivas analizadas: {binah_result['perspectives_count']}")
    print(f"  Riesgos sistemicos: {len(binah_result['systemic_risks'])} chars")

    # 4. CHESED - Identificar oportunidades de bondad
    print("\n[4/4] CHESED - Identificando oportunidades de bondad...")
    chesed = Chesed()

    chesed_input = {
        'stakeholders': binah_result['stakeholders'],
        'first_order_effects': binah_result['first_order_effects'],
        'second_order_effects': binah_result['second_order_effects'],
        'systemic_risks': binah_result['systemic_risks'],
        'ethical_considerations': binah_result['ethical_considerations'],
        'action': action_input['action']
    }

    chesed_result = chesed.process(chesed_input)

    if not chesed_result.get('processing_successful'):
        print(f"  ERROR en Chesed: {chesed_result.get('error')}")
        return

    # Mostrar resultados de Chesed
    print("\n" + "-"*80)
    print("RESULTADOS DE CHESED (Misericordia/Bondad)")
    print("-"*80)

    print(f"\nOPORTUNIDADES DE DAR ({len(chesed_result['giving_opportunities'])} identificadas):")
    for i, opp in enumerate(chesed_result['giving_opportunities'][:5], 1):
        print(f"  {i}. {opp}")

    print(f"\nBENEFICIARIOS:")
    beneficiaries = chesed_result['beneficiaries']
    if 'primary' in beneficiaries:
        print(f"  Primarios: {', '.join(beneficiaries['primary'][:3])}")
    if 'secondary' in beneficiaries:
        print(f"  Secundarios: {', '.join(beneficiaries['secondary'][:3])}")
    if 'tertiary' in beneficiaries:
        print(f"  Largo plazo: {', '.join(beneficiaries['tertiary'][:3])}")

    print(f"\nACCIONES GENEROSAS ({len(chesed_result['generous_actions'])} propuestas):")
    for i, action in enumerate(chesed_result['generous_actions'][:5], 1):
        print(f"  {i}. {action}")

    print(f"\nLIMITES NECESARIOS ({len(chesed_result['limits_needed'])} identificados):")
    for i, limit in enumerate(chesed_result['limits_needed'], 1):
        print(f"  {i}. {limit}")

    print(f"\nMETRICAS DE CHESED:")
    print(f"  Compassion Score: {chesed_result['compassion_score']*100:.1f}%")
    print(f"  Expansion Potential: {chesed_result['expansion_potential']*100:.1f}%")
    print(f"  Balance Awareness: {chesed_result['balance_awareness_score']*100:.1f}%")

    # Validar alineamiento de Chesed
    chesed_validation = chesed.validate_alignment()

    print(f"\nVALIDACION DE ALINEAMIENTO:")
    print(f"  Alineada: {chesed_validation['is_aligned']}")
    print(f"  Es compasiva: {chesed_validation['is_compassionate']}")
    print(f"  Esta balanceada: {chesed_validation['is_balanced']}")
    print(f"  Considera limites: {chesed_validation['considers_limits']}")
    print(f"  Status: {chesed_validation['status']}")

    # Resumen final
    print("\n" + "="*80)
    print("RESUMEN DEL FLUJO COMPLETO")
    print("="*80)
    print(f"1. KETER: {keter_result['alignment_score']*100:.1f}% alineamiento")
    print(f"2. CHOCHMAH: {chochmah_result['confidence_level']*100:.1f}% confianza")
    print(f"3. BINAH: {binah_result['perspectives_count']} perspectivas")
    print(f"4. CHESED: {len(chesed_result['giving_opportunities'])} oportunidades, {chesed_result['compassion_score']*100:.1f}% compasion")

    print("\n>> TEST EXITOSO" if chesed_validation['is_aligned'] else "\n>> ADVERTENCIA: Chesed requiere balance")
    print("="*80)


if __name__ == "__main__":
    test_chesed_basic()
