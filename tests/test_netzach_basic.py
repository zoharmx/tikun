"""
Test basico de Netzach (Victoria/Eternidad)
Verifica que la Sefira asegura persistencia y define condiciones de victoria
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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


def test_netzach_basic():
    """Test basico del flujo completo hasta Netzach"""

    print("\n" + "="*80)
    print("TEST BASICO NETZACH - Sistema Tikun Olam")
    print("NETZACH: Victoria y Persistencia (Venus)")
    print("="*80)

    # 1-6: Flujo anterior (resumido)
    print("\n[Ejecutando Keter -> Chochmah -> Binah -> Chesed -> Gevurah -> Tiferet...]")

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

    # 7. NETZACH - Asegurar persistencia y victoria
    print("\n[7/7] NETZACH - Victoria/Persistencia (Venus)...")
    print("  Asegurando sostenibilidad y momentum...")
    netzach = Netzach()

    netzach_input = {
        'balanced_decision': tiferet_result['balanced_decision'],
        'implementation_path': tiferet_result['implementation_path'],
        'harmony_score': tiferet_result['harmony_score'],
        'beauty_score': tiferet_result['beauty_score'],
        'action': action_input['action']
    }

    netzach_result = netzach.process(netzach_input)

    if not netzach_result.get('processing_successful'):
        print(f"  ERROR en Netzach: {netzach_result.get('error')}")
        return

    # Mostrar resultados de Netzach
    print("\n" + "-"*80)
    print("RESULTADOS DE NETZACH (Victoria/Persistencia - Venus)")
    print("-"*80)

    print(f"\nESTRATEGIA DE PERSISTENCIA:")
    strategy = netzach_result.get('persistence_strategy', '')
    if strategy:
        print(f"  {strategy[:250]}...")

    print(f"\nOBSTACULOS IDENTIFICADOS ({len(netzach_result['obstacles_identified'])}):")
    for i, obstacle in enumerate(netzach_result['obstacles_identified'][:5], 1):
        print(f"  {i}. {obstacle}")

    print(f"\nCONDICIONES DE VICTORIA ({len(netzach_result['victory_conditions'])}):")
    for i, condition in enumerate(netzach_result['victory_conditions'][:5], 1):
        print(f"  {i}. {condition}")

    print(f"\nMECANISMOS DE MOMENTUM ({len(netzach_result['momentum_mechanisms'])}):")
    for i, mechanism in enumerate(netzach_result['momentum_mechanisms'][:5], 1):
        print(f"  {i}. {mechanism}")

    print(f"\nPLAN DE RESISTENCIA:")
    endurance = netzach_result.get('endurance_plan', '')
    if endurance:
        print(f"  {endurance[:200]}...")

    print(f"\nMETRICAS DE NETZACH:")
    print(f"  Sustainability Score:    {netzach_result['sustainability_score']*100:.1f}%")
    print(f"  Victory Probability:     {netzach_result['victory_probability']*100:.1f}%")
    print(f"  Endurance Level:         {netzach_result['endurance_level']*100:.1f}%")

    # Validar alineamiento de Netzach
    netzach_validation = netzach.validate_alignment()

    print(f"\nVALIDACION DE ALINEAMIENTO:")
    print(f"  Alineada:               {netzach_validation['is_aligned']}")
    print(f"  Crea estrategia:        {netzach_validation['creates_strategy']}")
    print(f"  Identifica obstaculos:  {netzach_validation['identifies_obstacles']}")
    print(f"  Es sostenible:          {netzach_validation['is_sustainable']}")
    print(f"  Define victoria:        {netzach_validation['defines_victory']}")
    print(f"  Status:                 {netzach_validation['status']}")

    # Resumen final
    print("\n" + "="*80)
    print("RESUMEN DEL FLUJO COMPLETO (7 Sefirot)")
    print("="*80)
    print(f"1. KETER:    {keter_result['alignment_score']*100:.1f}% alineamiento")
    print(f"2. CHOCHMAH: {chochmah_result['confidence_level']*100:.1f}% confianza")
    print(f"3. BINAH:    {binah_result['perspectives_count']} perspectivas")
    print(f"4. CHESED:   {chesed_result['compassion_score']*100:.1f}% compasion (Jupiter)")
    print(f"5. GEVURAH:  {gevurah_result['severity_score']*100:.1f}% severidad (Marte)")
    print(f"6. TIFERET:  {tiferet_result['harmony_score']*100:.1f}% armonia (Sol)")
    print(f"7. NETZACH:  {netzach_result['sustainability_score']*100:.1f}% persistencia (Venus)")

    # Evaluar persistencia general
    if netzach_result['sustainability_score'] >= 0.7:
        persistence_status = "ALTA PERSISTENCIA - Victoria probable"
    elif netzach_result['sustainability_score'] >= 0.5:
        persistence_status = "PERSISTENCIA SOLIDA - Requiere atencion"
    else:
        persistence_status = "BAJA PERSISTENCIA - Riesgo de abandono"

    print(f"\n>> NETZACH: {persistence_status}")
    print(f">> Probabilidad Victoria: {netzach_result['victory_probability']*100:.1f}%")
    print(">> TEST EXITOSO" if netzach_validation['is_aligned'] else ">> ADVERTENCIA")
    print("="*80)


if __name__ == "__main__":
    test_netzach_basic()
