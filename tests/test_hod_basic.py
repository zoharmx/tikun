"""
Test basico de Hod (Esplendor/Gloria)
Verifica que la Sefira estructura y comunica con precision
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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


def test_hod_basic():
    """Test basico del flujo completo hasta Hod"""

    print("\n" + "="*80)
    print("TEST BASICO HOD - Sistema Tikun Olam")
    print("HOD: Estructura y Comunicacion (Mercurio)")
    print("="*80)

    # 1-7: Flujo anterior (resumido)
    print("\n[Ejecutando Keter -> Chochmah -> Binah -> Chesed -> Gevurah -> Tiferet -> Netzach...]")

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

    # 8. HOD - Estructurar y comunicar
    print("\n[8/8] HOD - Esplendor/Comunicacion (Mercurio)...")
    print("  Estructurando plan y creando comunicacion...")
    hod = Hod()

    hod_input = {
        'persistence_strategy': netzach_result['persistence_strategy'],
        'obstacles_identified': netzach_result['obstacles_identified'],
        'victory_conditions': netzach_result['victory_conditions'],
        'endurance_plan': netzach_result['endurance_plan'],
        'momentum_mechanisms': netzach_result['momentum_mechanisms'],
        'sustainability_score': netzach_result['sustainability_score'],
        'action': action_input['action']
    }

    hod_result = hod.process(hod_input)

    if not hod_result.get('processing_successful'):
        print(f"  ERROR en Hod: {hod_result.get('error')}")
        return

    # Mostrar resultados de Hod
    print("\n" + "-"*80)
    print("RESULTADOS DE HOD (Esplendor/Gloria - Mercurio)")
    print("-"*80)

    print(f"\nPLAN ESTRUCTURADO:")
    plan = hod_result.get('structured_plan', {})
    phase_count = len([k for k in plan.keys() if 'phase' in k])
    print(f"  Fases identificadas: {phase_count}")
    for phase_key, phase_data in list(plan.items())[:3]:
        if isinstance(phase_data, dict):
            content = phase_data.get('content', str(phase_data))[:150]
            print(f"  - {phase_key}: {content}...")

    print(f"\nESTRATEGIA DE COMUNICACION:")
    comm_strategy = hod_result.get('communication_strategy', {})
    stakeholders = comm_strategy.get('stakeholders', [])
    print(f"  Stakeholders: {', '.join(stakeholders) if stakeholders else 'No especificados'}")
    comm_desc = comm_strategy.get('description', '')
    if comm_desc:
        print(f"  {comm_desc[:200]}...")

    print(f"\nFRAMEWORK DE METRICAS:")
    metrics = hod_result.get('metrics_framework', {})
    kpis = metrics.get('kpis', [])
    print(f"  KPIs definidos: {len(kpis)}")
    for i, kpi in enumerate(kpis[:5], 1):
        print(f"  {i}. {kpi[:150]}")

    print(f"\nDOCUMENTACION ({len(hod_result['documentation'])} documentos):")
    for i, doc in enumerate(hod_result['documentation'][:5], 1):
        print(f"  {i}. {doc}")

    print(f"\nMENSAJES STAKEHOLDERS ({len(hod_result['stakeholder_messages'])} mensajes):")
    for stakeholder, message in list(hod_result['stakeholder_messages'].items())[:3]:
        print(f"  {stakeholder.capitalize()}: {message[:100]}...")

    print(f"\nMETRICAS DE HOD:")
    print(f"  Precision Score:         {hod_result['precision_score']*100:.1f}%")
    print(f"  Clarity Score:           {hod_result['clarity_score']*100:.1f}%")

    # Validar alineamiento de Hod
    hod_validation = hod.validate_alignment()

    print(f"\nVALIDACION DE ALINEAMIENTO:")
    print(f"  Alineada:                {hod_validation['is_aligned']}")
    print(f"  Estructura planes:       {hod_validation['structures_plans']}")
    print(f"  Comunica claramente:     {hod_validation['communicates_clearly']}")
    print(f"  Es precisa:              {hod_validation['is_precise']}")
    print(f"  Define metricas:         {hod_validation['defines_metrics']}")
    print(f"  Status:                  {hod_validation['status']}")

    # Resumen final
    print("\n" + "="*80)
    print("RESUMEN DEL FLUJO COMPLETO (8 Sefirot)")
    print("="*80)
    print(f"1. KETER:    {keter_result['alignment_score']*100:.1f}% alineamiento")
    print(f"2. CHOCHMAH: {chochmah_result['confidence_level']*100:.1f}% confianza")
    print(f"3. BINAH:    {binah_result['perspectives_count']} perspectivas")
    print(f"4. CHESED:   {chesed_result['compassion_score']*100:.1f}% compasion (Jupiter)")
    print(f"5. GEVURAH:  {gevurah_result['severity_score']*100:.1f}% severidad (Marte)")
    print(f"6. TIFERET:  {tiferet_result['harmony_score']*100:.1f}% armonia (Sol)")
    print(f"7. NETZACH:  {netzach_result['sustainability_score']*100:.1f}% persistencia (Venus)")
    print(f"8. HOD:      {hod_result['precision_score']*100:.1f}% precision (Mercurio)")

    # Evaluar estructura y comunicacion
    if hod_result['precision_score'] >= 0.7 and hod_result['clarity_score'] >= 0.7:
        structure_status = "ALTA PRECISION - Estructura mercurial excelente"
    elif hod_result['precision_score'] >= 0.5:
        structure_status = "PRECISION SOLIDA - Estructura aceptable"
    else:
        structure_status = "BAJA PRECISION - Requiere mas estructura"

    print(f"\n>> HOD: {structure_status}")
    print(f">> Precision: {hod_result['precision_score']*100:.1f}% | Claridad: {hod_result['clarity_score']*100:.1f}%")
    print(">> TEST EXITOSO" if hod_validation['is_aligned'] else ">> ADVERTENCIA")
    print("="*80)


if __name__ == "__main__":
    test_hod_basic()
