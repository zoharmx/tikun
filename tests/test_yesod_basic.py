"""
Test basico de Yesod (Fundamento/Fundacion)
Verifica que la Sefira conecta plan con realidad y prepara manifestacion
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.sefirot.yesod import Yesod
from src.sefirot.hod import Hod
from src.sefirot.netzach import Netzach
from src.sefirot.tiferet import Tiferet
from src.sefirot.gevurah import Gevurah
from src.sefirot.chesed import Chesed
from src.sefirot.binah import Binah
from src.sefirot.chochmah_gemini import ChochmahGemini
from src.sefirot.keter import Keter
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()


def test_yesod_basic():
    """Test basico del flujo completo hasta Yesod"""

    print("\n" + "="*80)
    print("TEST BASICO YESOD - Sistema Tikun Olam")
    print("YESOD: Fundamento y Conexion (Luna)")
    print("="*80)

    # 1-8: Flujo anterior (resumido)
    print("\n[Ejecutando Keter -> Chochmah -> Binah -> Chesed -> Gevurah -> Tiferet -> Netzach -> Hod...]")

    keter = Keter(use_llm_scoring=True)
    action_input = {
        'action': 'Implementar sistema de IA educativa en comunidades rurales',
        'context': 'Comunidades con acceso limitado a educacion de calidad',
        'expected_outcome': 'Mejorar alfabetizacion digital y acceso a conocimiento'
    }
    keter_result = keter.process(action_input)

    chochmah = ChochmahGemini()
    chochmah_result = chochmah.process({
        'query': action_input['action'],
        'context': action_input['context']
    })

    binah = Binah()
    binah_result = binah.process({
        'understanding': chochmah_result['understanding'],
        'analysis': chochmah_result['analysis'],
        'action': action_input['action']
    })

    chesed = Chesed()
    chesed_result = chesed.process({
        'stakeholders': binah_result['stakeholders'],
        'first_order_effects': binah_result['first_order_effects'],
        'second_order_effects': binah_result['second_order_effects'],
        'systemic_risks': binah_result['systemic_risks'],
        'ethical_considerations': binah_result['ethical_considerations'],
        'action': action_input['action']
    })

    gevurah = Gevurah()
    gevurah_result = gevurah.process({
        'giving_opportunities': chesed_result['giving_opportunities'],
        'beneficiaries': chesed_result['beneficiaries'],
        'generous_actions': chesed_result['generous_actions'],
        'compassion_score': chesed_result['compassion_score'],
        'expansion_potential': chesed_result['expansion_potential'],
        'limits_needed': chesed_result['limits_needed'],
        'action': action_input['action']
    })

    tiferet = Tiferet()
    tiferet_result = tiferet.process({
        'chesed_output': chesed_result,
        'gevurah_output': gevurah_result,
        'action': action_input['action']
    })

    print(f"  Tiferet Harmony: {tiferet_result['harmony_score']*100:.1f}%")

    netzach = Netzach()
    netzach_result = netzach.process({
        'balanced_decision': tiferet_result['balanced_decision'],
        'implementation_path': tiferet_result['implementation_path'],
        'harmony_score': tiferet_result['harmony_score'],
        'beauty_score': tiferet_result['beauty_score'],
        'action': action_input['action']
    })

    print(f"  Netzach Sustainability: {netzach_result['sustainability_score']*100:.1f}%")

    hod = Hod()
    hod_result = hod.process({
        'persistence_strategy': netzach_result['persistence_strategy'],
        'obstacles_identified': netzach_result['obstacles_identified'],
        'victory_conditions': netzach_result['victory_conditions'],
        'endurance_plan': netzach_result['endurance_plan'],
        'momentum_mechanisms': netzach_result['momentum_mechanisms'],
        'sustainability_score': netzach_result['sustainability_score'],
        'action': action_input['action']
    })

    print(f"  Hod Precision: {hod_result['precision_score']*100:.1f}%")

    # 9. YESOD - Fundar y conectar con realidad
    print("\n[9/9] YESOD - Fundamento/Conexion (Luna)...")
    print("  Conectando plan con realidad y preparando manifestacion...")
    yesod = Yesod()

    yesod_input = {
        'structured_plan': hod_result['structured_plan'],
        'communication_strategy': hod_result['communication_strategy'],
        'metrics_framework': hod_result['metrics_framework'],
        'documentation': hod_result['documentation'],
        'stakeholder_messages': hod_result['stakeholder_messages'],
        'precision_score': hod_result['precision_score'],
        'clarity_score': hod_result['clarity_score'],
        'action': action_input['action']
    }

    yesod_result = yesod.process(yesod_input)

    if not yesod_result.get('processing_successful'):
        print(f"  ERROR en Yesod: {yesod_result.get('error')}")
        return

    # Mostrar resultados de Yesod
    print("\n" + "-"*80)
    print("RESULTADOS DE YESOD (Fundamento/Fundacion - Luna)")
    print("-"*80)

    print(f"\nEVALUACION DE FUNDAMENTOS:")
    foundation = yesod_result.get('foundation_assessment', {})
    solidity = foundation.get('solidity', 0.0)
    print(f"  Solidez: {solidity*100:.1f}%")
    gaps = foundation.get('gaps', [])
    if gaps:
        print(f"  Gaps identificados: {len(gaps)}")
        for i, gap in enumerate(gaps[:3], 1):
            print(f"    {i}. {gap[:100]}...")
    strengths = foundation.get('strengths', [])
    if strengths:
        print(f"  Fortalezas: {len(strengths)}")

    print(f"\nCONEXION CON REALIDAD:")
    reality = yesod_result.get('reality_connection', {})
    concrete = reality.get('concrete_elements', [])
    print(f"  Elementos concretos: {len(concrete)}")
    if reality.get('description'):
        print(f"  {reality['description'][:200]}...")

    print(f"\nPRIMEROS PASOS CONCRETOS ({len(yesod_result['first_concrete_steps'])} pasos):")
    for i, step in enumerate(yesod_result['first_concrete_steps'][:7], 1):
        action = step.get('action', str(step))
        week = step.get('week', '?')
        print(f"  {i}. [Semana {week}] {action[:120]}")

    print(f"\nREQUISITOS DE RECURSOS:")
    resources = yesod_result.get('resource_requirements', {})
    budget = resources.get('budget', [])
    personnel = resources.get('personnel', [])
    infra = resources.get('infrastructure', [])
    print(f"  Presupuesto items: {len(budget)}")
    print(f"  Personal items: {len(personnel)}")
    print(f"  Infraestructura items: {len(infra)}")
    if budget:
        print(f"    Budget: {budget[0][:100]}...")
    if personnel:
        print(f"    Personal: {personnel[0][:100]}...")

    print(f"\nALINEAMIENTO STAKEHOLDERS ({len(yesod_result['stakeholder_alignment'])} stakeholders):")
    for stakeholder, info in list(yesod_result['stakeholder_alignment'].items())[:5]:
        status = info.get('status', 'Unknown')
        print(f"  {stakeholder.capitalize()}: {status}")

    print(f"\nMETRICAS DE YESOD:")
    print(f"  Manifestation Readiness: {yesod_result['manifestation_readiness']*100:.1f}%")
    print(f"  Integration Score:       {yesod_result['integration_score']*100:.1f}%")
    print(f"  Ready to Manifest:       {yesod_result['ready_to_manifest']}")

    # Validar alineamiento de Yesod
    yesod_validation = yesod.validate_alignment()

    print(f"\nVALIDACION DE ALINEAMIENTO:")
    print(f"  Alineada:                {yesod_validation['is_aligned']}")
    print(f"  Valida fundamentos:      {yesod_validation['validates_foundations']}")
    print(f"  Conecta con realidad:    {yesod_validation['connects_to_reality']}")
    print(f"  Esta lista:              {yesod_validation['is_ready']}")
    print(f"  Define pasos:            {yesod_validation['defines_steps']}")
    print(f"  Status:                  {yesod_validation['status']}")

    # Resumen final
    print("\n" + "="*80)
    print("RESUMEN DEL FLUJO COMPLETO (9 Sefirot)")
    print("="*80)
    print(f"1. KETER:    {keter_result['alignment_score']*100:.1f}% alineamiento")
    print(f"2. CHOCHMAH: {chochmah_result['confidence_level']*100:.1f}% confianza")
    print(f"3. BINAH:    {binah_result['perspectives_count']} perspectivas")
    print(f"4. CHESED:   {chesed_result['compassion_score']*100:.1f}% compasion (Jupiter)")
    print(f"5. GEVURAH:  {gevurah_result['severity_score']*100:.1f}% severidad (Marte)")
    print(f"6. TIFERET:  {tiferet_result['harmony_score']*100:.1f}% armonia (Sol)")
    print(f"7. NETZACH:  {netzach_result['sustainability_score']*100:.1f}% persistencia (Venus)")
    print(f"8. HOD:      {hod_result['precision_score']*100:.1f}% precision (Mercurio)")
    print(f"9. YESOD:    {yesod_result['manifestation_readiness']*100:.1f}% readiness (Luna)")

    # Evaluar fundamento y preparacion
    if yesod_result['manifestation_readiness'] >= 0.75 and yesod_result['ready_to_manifest']:
        foundation_status = "FUNDAMENTO SOLIDO - Listo para manifestar"
    elif yesod_result['manifestation_readiness'] >= 0.6:
        foundation_status = "FUNDAMENTO ACEPTABLE - Requiere ajustes menores"
    else:
        foundation_status = "FUNDAMENTO DEBIL - Requiere mas preparacion"

    print(f"\n>> YESOD: {foundation_status}")
    print(f">> Readiness: {yesod_result['manifestation_readiness']*100:.1f}% | Integration: {yesod_result['integration_score']*100:.1f}%")
    print(f">> Pasos concretos: {len(yesod_result['first_concrete_steps'])}")
    print(">> TEST EXITOSO" if yesod_validation['is_aligned'] else ">> ADVERTENCIA")
    print("="*80)


if __name__ == "__main__":
    test_yesod_basic()
