"""
Test basico de Gevurah (Severidad/Juicio)
Verifica que la Sefira aplica limites necesarios y balancea con Chesed
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.sefirot.gevurah import Gevurah
from src.sefirot.chesed import Chesed
from src.sefirot.binah import Binah
from src.sefirot.chochmah_gemini import ChochmahGemini
from src.sefirot.keter import Keter
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()


def test_gevurah_basic():
    """Test basico del flujo completo hasta Gevurah"""

    print("\n" + "="*80)
    print("TEST BASICO GEVURAH - Sistema Tikun Olam")
    print("="*80)

    # 1. KETER - Define objetivo
    print("\n[1/5] KETER - Evaluando alineamiento con Tikun Olam...")
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
    print("\n[2/5] CHOCHMAH - Razonamiento profundo...")
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

    # 3. BINAH - Analisis contextual
    print("\n[3/5] BINAH - Analisis contextual...")
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

    # 4. CHESED - Identificar oportunidades de bondad
    print("\n[4/5] CHESED - Identificando oportunidades de bondad...")
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

    print(f"  Oportunidades identificadas: {len(chesed_result['giving_opportunities'])}")
    print(f"  Compassion Score: {chesed_result['compassion_score']*100:.1f}%")

    # 5. GEVURAH - Aplicar limites y juicio
    print("\n[5/5] GEVURAH - Aplicando limites y juicio...")
    gevurah = Gevurah()

    gevurah_input = {
        'giving_opportunities': chesed_result['giving_opportunities'],
        'beneficiaries': chesed_result['beneficiaries'],
        'generous_actions': chesed_result['generous_actions'],
        'compassion_score': chesed_result['compassion_score'],
        'expansion_potential': chesed_result['expansion_potential'],
        'limits_needed': chesed_result['limits_needed'],
        'action': action_input['action']
    }

    gevurah_result = gevurah.process(gevurah_input)

    if not gevurah_result.get('processing_successful'):
        print(f"  ERROR en Gevurah: {gevurah_result.get('error')}")
        return

    # Mostrar resultados de Gevurah
    print("\n" + "-"*80)
    print("RESULTADOS DE GEVURAH (Severidad/Juicio)")
    print("-"*80)

    print(f"\nEXCESOS DE CHESED ({len(gevurah_result['chesed_excesses'])} identificados):")
    for i, excess in enumerate(gevurah_result['chesed_excesses'][:5], 1):
        print(f"  {i}. {excess}")

    print(f"\nLIMITES NECESARIOS ({len(gevurah_result['necessary_boundaries'])} identificados):")
    for i, boundary in enumerate(gevurah_result['necessary_boundaries'][:5], 1):
        print(f"  {i}. {boundary}")

    print(f"\nCRITERIOS DE JUSTICIA ({len(gevurah_result['justice_criteria'])} aplicados):")
    for i, criterion in enumerate(gevurah_result['justice_criteria'][:5], 1):
        print(f"  {i}. {criterion}")

    print(f"\nRESTRICCIONES ({len(gevurah_result['restrictions'])} aplicadas):")
    for i, restriction in enumerate(gevurah_result['restrictions'][:5], 1):
        print(f"  {i}. {restriction}")

    print(f"\nADVERTENCIAS ({len(gevurah_result['warnings'])} emitidas):")
    for i, warning in enumerate(gevurah_result['warnings'], 1):
        print(f"  {i}. {warning}")

    print(f"\nMETRICAS DE GEVURAH:")
    print(f"  Severity Score: {gevurah_result['severity_score']*100:.1f}%")
    print(f"  Balance con Chesed: {gevurah_result['balance_with_chesed']*100:.1f}%")

    # Validar alineamiento de Gevurah
    gevurah_validation = gevurah.validate_alignment()

    print(f"\nVALIDACION DE ALINEAMIENTO:")
    print(f"  Alineada: {gevurah_validation['is_aligned']}")
    print(f"  Es severa: {gevurah_validation['is_severe']}")
    print(f"  Esta balanceada: {gevurah_validation['is_balanced']}")
    print(f"  Advierte apropiadamente: {gevurah_validation['warns_appropriately']}")
    print(f"  Status: {gevurah_validation['status']}")

    # Analisis de balance Chesed-Gevurah
    print("\n" + "-"*80)
    print("BALANCE CHESED-GEVURAH")
    print("-"*80)
    print(f"  CHESED (Misericordia): {chesed_result['compassion_score']*100:.1f}%")
    print(f"  GEVURAH (Severidad):   {gevurah_result['severity_score']*100:.1f}%")
    print(f"  Balance Score:         {gevurah_result['balance_with_chesed']*100:.1f}%")

    balance_diff = abs(chesed_result['compassion_score'] - gevurah_result['severity_score'])
    if balance_diff < 0.2:
        balance_status = "EXCELENTE BALANCE"
    elif balance_diff < 0.3:
        balance_status = "BUEN BALANCE"
    elif balance_diff < 0.5:
        balance_status = "BALANCE ACEPTABLE"
    else:
        balance_status = "DESBALANCEADO"

    print(f"  Diferencia:            {balance_diff*100:.1f}%")
    print(f"  Status:                {balance_status}")

    # Resumen final
    print("\n" + "="*80)
    print("RESUMEN DEL FLUJO COMPLETO")
    print("="*80)
    print(f"1. KETER:    {keter_result['alignment_score']*100:.1f}% alineamiento")
    print(f"2. CHOCHMAH: {chochmah_result['confidence_level']*100:.1f}% confianza")
    print(f"3. BINAH:    {binah_result['perspectives_count']} perspectivas")
    print(f"4. CHESED:   {len(chesed_result['giving_opportunities'])} oportunidades, {chesed_result['compassion_score']*100:.1f}% compasion")
    print(f"5. GEVURAH:  {len(gevurah_result['necessary_boundaries'])} limites, {gevurah_result['severity_score']*100:.1f}% severidad")

    print("\n>> BALANCE: " + balance_status)
    print(">> TEST EXITOSO" if gevurah_validation['is_aligned'] else ">> ADVERTENCIA: Gevurah requiere ajuste")
    print("="*80)


if __name__ == "__main__":
    test_gevurah_basic()
