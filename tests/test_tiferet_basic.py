"""
Test basico de Tiferet (Belleza/Armonia)
Verifica que la Sefira sintetiza Chesed y Gevurah armonicamente
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.sefirot.tiferet import Tiferet
from src.sefirot.gevurah import Gevurah
from src.sefirot.chesed import Chesed
from src.sefirot.binah import Binah
from src.sefirot.chochmah_gemini import ChochmahGemini
from src.sefirot.keter import Keter
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()


def test_tiferet_basic():
    """Test basico del flujo completo hasta Tiferet"""

    print("\n" + "="*80)
    print("TEST BASICO TIFERET - Sistema Tikun Olam")
    print("TIFERET: El Corazon Solar del Sistema")
    print("="*80)

    # 1. KETER - Define objetivo
    print("\n[1/6] KETER - Evaluando alineamiento con Tikun Olam...")
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
    print("\n[2/6] CHOCHMAH - Razonamiento profundo...")
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
    print("\n[3/6] BINAH - Analisis contextual...")
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

    print(f"  Perspectivas: {binah_result['perspectives_count']}")

    # 4. CHESED - Identificar oportunidades de bondad
    print("\n[4/6] CHESED - Misericordia/Bondad (Jupiter)...")
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

    print(f"  Compassion Score: {chesed_result['compassion_score']*100:.1f}%")
    print(f"  Oportunidades: {len(chesed_result['giving_opportunities'])}")

    # 5. GEVURAH - Aplicar limites y juicio
    print("\n[5/6] GEVURAH - Severidad/Juicio (Marte)...")
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

    print(f"  Severity Score: {gevurah_result['severity_score']*100:.1f}%")
    print(f"  Limites: {len(gevurah_result['necessary_boundaries'])}")

    # 6. TIFERET - Sintesis armonica
    print("\n[6/6] TIFERET - Belleza/Armonia (Sol)...")
    print("  Sintetizando Chesed + Gevurah...")
    tiferet = Tiferet()

    tiferet_input = {
        'chesed_output': chesed_result,
        'gevurah_output': gevurah_result,
        'action': action_input['action']
    }

    tiferet_result = tiferet.process(tiferet_input)
    if not tiferet_result.get('processing_successful'):
        print(f"  ERROR en Tiferet: {tiferet_result.get('error')}")
        return

    # Mostrar resultados de Tiferet
    print("\n" + "-"*80)
    print("RESULTADOS DE TIFERET (Belleza/Armonia - Corazon Solar)")
    print("-"*80)

    print(f"\nSINTESIS CHESED-GEVURAH:")
    synthesis = tiferet_result.get('synthesis', '')
    if synthesis:
        # Mostrar primeras 300 chars
        print(f"  {synthesis[:300]}...")

    print(f"\nCONFLICTOS RESUELTOS ({len(tiferet_result['conflicts_resolved'])}):")
    for i, conflict in enumerate(tiferet_result['conflicts_resolved'][:5], 1):
        print(f"  {i}. {conflict}")

    print(f"\nDECISION BALANCEADA:")
    decision = tiferet_result.get('balanced_decision', '')
    if decision:
        # Mostrar primeras 200 chars
        print(f"  {decision[:200]}...")

    print(f"\nINTEGRACION DE CHESED (Misericordia):")
    chesed_int = tiferet_result.get('chesed_integration', '')
    if chesed_int:
        print(f"  {chesed_int[:150]}...")

    print(f"\nINTEGRACION DE GEVURAH (Juicio):")
    gevurah_int = tiferet_result.get('gevurah_integration', '')
    if gevurah_int:
        print(f"  {gevurah_int[:150]}...")

    print(f"\nCAMINO DE IMPLEMENTACION ({len(tiferet_result['implementation_path'])} pasos):")
    for i, step in enumerate(tiferet_result['implementation_path'][:5], 1):
        print(f"  {i}. {step}")

    print(f"\nMETRICAS DE TIFERET:")
    print(f"  Harmony Score:        {tiferet_result['harmony_score']*100:.1f}%")
    print(f"  Beauty Score:         {tiferet_result['beauty_score']*100:.1f}%")
    print(f"  Balance C-G:          {tiferet_result['chesed_gevurah_balance']*100:.1f}%")
    print(f"  Radiance:             {tiferet_result['radiance']*100:.1f}%")
    print(f"  Synthesis Quality:    {tiferet_result['synthesis_quality']}")

    # Validar alineamiento de Tiferet
    tiferet_validation = tiferet.validate_alignment()

    print(f"\nVALIDACION DE ALINEAMIENTO:")
    print(f"  Alineada:             {tiferet_validation['is_aligned']}")
    print(f"  Crea sintesis:        {tiferet_validation['creates_synthesis']}")
    print(f"  Es armoniosa:         {tiferet_validation['is_harmonious']}")
    print(f"  Integra ambos:        {tiferet_validation['integrates_both']}")
    print(f"  Resuelve conflictos:  {tiferet_validation['resolves_conflicts']}")
    print(f"  Status:               {tiferet_validation['status']}")

    # Analisis del balance final
    print("\n" + "-"*80)
    print("BALANCE FINAL DEL SISTEMA (Sefirot Emocionales)")
    print("-"*80)
    print(f"  CHESED (Misericordia/Jupiter):  {chesed_result['compassion_score']*100:.1f}%")
    print(f"  GEVURAH (Severidad/Marte):      {gevurah_result['severity_score']*100:.1f}%")
    print(f"  TIFERET (Armonia/Sol):          {tiferet_result['harmony_score']*100:.1f}%")
    print(f"")
    print(f"  Balance Chesed-Gevurah:         {tiferet_result['chesed_gevurah_balance']*100:.1f}%")
    print(f"  Belleza de sintesis:            {tiferet_result['beauty_score']*100:.1f}%")

    # Determinar calidad del balance
    harmony = tiferet_result['harmony_score']
    beauty = tiferet_result['beauty_score']

    if harmony > 0.8 and beauty > 0.8:
        balance_quality = "EXCELENTE - Sintesis solar perfecta"
    elif harmony > 0.7 and beauty > 0.7:
        balance_quality = "MUY BUENO - Armonia fuerte"
    elif harmony > 0.6 and beauty > 0.6:
        balance_quality = "BUENO - Balance solido"
    else:
        balance_quality = "ACEPTABLE - Requiere refinamiento"

    print(f"")
    print(f"  Calidad del Balance:            {balance_quality}")

    # Resumen final
    print("\n" + "="*80)
    print("RESUMEN DEL FLUJO COMPLETO")
    print("="*80)
    print(f"1. KETER:    {keter_result['alignment_score']*100:.1f}% alineamiento")
    print(f"2. CHOCHMAH: {chochmah_result['confidence_level']*100:.1f}% confianza")
    print(f"3. BINAH:    {binah_result['perspectives_count']} perspectivas")
    print(f"4. CHESED:   {chesed_result['compassion_score']*100:.1f}% compasion (Jupiter)")
    print(f"5. GEVURAH:  {gevurah_result['severity_score']*100:.1f}% severidad (Marte)")
    print(f"6. TIFERET:  {tiferet_result['harmony_score']*100:.1f}% armonia (Sol)")

    print("\n>> TIFERET: " + balance_quality)
    print(">> TEST EXITOSO" if tiferet_validation['is_aligned'] else ">> ADVERTENCIA: Tiferet requiere ajuste")
    print("="*80)


if __name__ == "__main__":
    test_tiferet_basic()
