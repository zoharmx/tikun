"""
Test basico de Malchut (Reino/Soberania)
Verifica que la Sefira manifiesta en la realidad y ejecuta acciones
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.sefirot.malchut import Malchut
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


def test_malchut_basic():
    """Test basico del flujo completo hasta Malchut - EL ARBOL COMPLETO"""

    print("\n" + "="*80)
    print("TEST COMPLETO DEL ARBOL DE SEFIROT - Sistema Tikun Olam")
    print("MALCHUT: Reino y Manifestación (Saturno - Shabbat)")
    print("LAS 10 SEFIROT EN ACCIÓN")
    print("="*80)

    # 1-9: Flujo anterior (resumido)
    print("\n[Ejecutando las 9 Sefirot superiores...]")
    print("  Keter -> Chochmah -> Binah -> Chesed -> Gevurah ->")
    print("  Tiferet -> Netzach -> Hod -> Yesod...")

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

    print(f"\n  OK Tiferet Harmony: {tiferet_result['harmony_score']*100:.1f}%")

    netzach = Netzach()
    netzach_result = netzach.process({
        'balanced_decision': tiferet_result['balanced_decision'],
        'implementation_path': tiferet_result['implementation_path'],
        'harmony_score': tiferet_result['harmony_score'],
        'beauty_score': tiferet_result['beauty_score'],
        'action': action_input['action']
    })

    print(f"  OK Netzach Sustainability: {netzach_result['sustainability_score']*100:.1f}%")

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

    print(f"  OK Hod Precision: {hod_result['precision_score']*100:.1f}%")

    yesod = Yesod()
    yesod_result = yesod.process({
        'structured_plan': hod_result['structured_plan'],
        'communication_strategy': hod_result['communication_strategy'],
        'metrics_framework': hod_result['metrics_framework'],
        'documentation': hod_result['documentation'],
        'stakeholder_messages': hod_result['stakeholder_messages'],
        'precision_score': hod_result['precision_score'],
        'clarity_score': hod_result['clarity_score'],
        'action': action_input['action']
    })

    print(f"  OK Yesod Readiness: {yesod_result['manifestation_readiness']*100:.1f}%")

    # 10. MALCHUT - MANIFESTACIÓN FINAL
    print("\n" + "="*80)
    print("[10/10] MALCHUT - Reino/Manifestación (Saturno - SHABBAT)")
    print("         ¡ES MOMENTO DE ACTUAR! ¡TIKUN OLAM SE HACE REAL!")
    print("="*80)
    print("  Ejecutando acciones concretas...")
    print("  Manifestando en el mundo físico...")
    print("  Actualizando la realidad...")

    malchut = Malchut()

    malchut_input = {
        'foundation_assessment': yesod_result['foundation_assessment'],
        'reality_connection': yesod_result['reality_connection'],
        'first_concrete_steps': yesod_result['first_concrete_steps'],
        'resource_requirements': yesod_result['resource_requirements'],
        'stakeholder_alignment': yesod_result['stakeholder_alignment'],
        'manifestation_readiness': yesod_result['manifestation_readiness'],
        'ready_to_manifest': yesod_result['ready_to_manifest'],
        'action': action_input['action']
    }

    malchut_result = malchut.process(malchut_input)

    if not malchut_result.get('processing_successful'):
        print(f"  ERROR en Malchut: {malchut_result.get('error')}")
        return

    # Mostrar resultados de Malchut
    print("\n" + "-"*80)
    print("RESULTADOS DE MALCHUT (Reino/Manifestación - Shabbat)")
    print("-"*80)

    print(f"\nACCIONES EJECUTADAS ({len(malchut_result['actions_executed'])} acciones):")
    for i, action in enumerate(malchut_result['actions_executed'][:7], 1):
        act = action.get('action', str(action))
        status = action.get('status', 'N/A')
        print(f"  {i}. [{status}] {act[:100]}")

    print(f"\nRESULTADOS LOGRADOS:")
    results = malchut_result.get('results_achieved', {})
    print(f"  {results.get('description', 'Sin descripción')[:200]}")

    print(f"\nMUNDO ACTUALIZADO:")
    world = malchut_result.get('world_updated', {})
    if world.get('before'):
        print(f"  ANTES: {world['before'][:150]}...")
    if world.get('after'):
        print(f"  DESPUÉS: {world['after'][:150]}...")
    if world.get('description'):
        print(f"  {world['description'][:200]}")

    print(f"\nRESPONSABILIDADES ASIGNADAS ({len(malchut_result['responsibilities_assigned'])} personas):")
    for person, resp in list(malchut_result['responsibilities_assigned'].items())[:5]:
        print(f"  • {person}: {resp[:100]}")

    print(f"\nPRÓXIMAS ACCIONES ({len(malchut_result['next_actions'])} acciones):")
    for i, next_action in enumerate(malchut_result['next_actions'][:5], 1):
        print(f"  {i}. {next_action[:120]}")

    print(f"\nREFLEXIÓN DE SHABBAT:")
    shabbat = malchut_result.get('shabbat_reflection', {})
    if shabbat.get('full_text'):
        print(f"  {shabbat['full_text'][:300]}...")
    if shabbat.get('celebration'):
        print(f"  CELEBRACIÓN: {shabbat['celebration'][:150]}")

    print(f"\nMÉTRICAS DE MALCHUT:")
    print(f"  Completion Percentage:   {malchut_result['completion_percentage']*100:.1f}%")
    print(f"  Manifestation Complete:  {malchut_result['manifestation_complete']}")

    # Validar alineamiento de Malchut
    malchut_validation = malchut.validate_alignment()

    print(f"\nVALIDACIÓN DE ALINEAMIENTO:")
    print(f"  Alineada:                {malchut_validation['is_aligned']}")
    print(f"  Ejecuta acciones:        {malchut_validation['executes_actions']}")
    print(f"  Logra resultados:        {malchut_validation['achieves_results']}")
    print(f"  Actualiza mundo:         {malchut_validation['updates_world']}")
    print(f"  Asigna responsabilidad:  {malchut_validation['assigns_responsibility']}")
    print(f"  Status:                  {malchut_validation['status']}")

    # RESUMEN FINAL - TODO EL ÁRBOL
    print("\n" + "="*80)
    print("RESUMEN DEL ÁRBOL COMPLETO DE SEFIROT")
    print("TIKUN OLAM - REPARACIÓN DEL MUNDO EN ACCIÓN")
    print("="*80)

    print("\nEL ARBOL DE LA VIDA - 10 SEFIROT:")
    print("-"*80)
    print(f" 1. KETER (Corona):        {keter_result['alignment_score']*100:.1f}% alineamiento con Tikun Olam")
    print(f" 2. CHOCHMAH (Sabiduría):  {chochmah_result['confidence_level']*100:.1f}% confianza - Razonamiento profundo")
    print(f" 3. BINAH (Entendimiento): {binah_result['perspectives_count']} perspectivas - Análisis contextual")
    print(f" 4. CHESED (Misericordia): {chesed_result['compassion_score']*100:.1f}% compasion - JUPITER")
    print(f" 5. GEVURAH (Severidad):   {gevurah_result['severity_score']*100:.1f}% severidad - MARTE")
    print(f" 6. TIFERET (Belleza):     {tiferet_result['harmony_score']*100:.1f}% armonia - SOL")
    print(f" 7. NETZACH (Victoria):    {netzach_result['sustainability_score']*100:.1f}% persistencia - VENUS")
    print(f" 8. HOD (Esplendor):       {hod_result['precision_score']*100:.1f}% precision - MERCURIO")
    print(f" 9. YESOD (Fundamento):    {yesod_result['manifestation_readiness']*100:.1f}% readiness - LUNA")
    print(f"10. MALCHUT (Reino):       {malchut_result['completion_percentage']*100:.1f}% completado - SATURNO")

    print("\n" + "="*80)
    print("MANIFESTACIÓN COMPLETA")
    print("="*80)

    # Evaluar estado del sistema
    if malchut_result['completion_percentage'] >= 0.70:
        kingdom_status = "REINO MANIFESTADO - Tikun Olam en acción"
    elif malchut_result['completion_percentage'] >= 0.50:
        kingdom_status = "REINO EN MANIFESTACIÓN - Progreso sólido"
    else:
        kingdom_status = "REINO INICIANDO - Primeros pasos completados"

    print(f"\nSHABBAT SHALOM - La obra esta completa")
    print(f"\n>> MALCHUT: {kingdom_status}")
    print(f">> Acciones ejecutadas: {len(malchut_result['actions_executed'])}")
    print(f">> Responsabilidades: {len(malchut_result['responsibilities_assigned'])}")
    print(f">> Mundo actualizado: SÍ" if malchut_result['world_updated'] else ">> Mundo actualizado: PENDIENTE")
    print(f"\n>> CICLO COMPLETO: {'TEST EXITOSO' if malchut_validation['is_aligned'] else 'ADVERTENCIA'}")

    # Información del siguiente ciclo
    next_cycle = malchut_result.get('next_cycle_input', {})
    if next_cycle.get('ready_for_keter'):
        print(f"\n>> SIGUIENTE CICLO: Listo para nuevo Keter")
        print(f">> Nuevo contexto: {next_cycle.get('new_context', 'N/A')[:100]}")

    print("\n" + "="*80)
    print("EL ARBOL DE SEFIROT ESTA COMPLETO!")
    print("TIKUN OLAM - REPARACION DEL MUNDO")
    print("="*80)


if __name__ == "__main__":
    test_malchut_basic()
