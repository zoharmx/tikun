"""
Test de Métricas del Mundo de Atzilut
Valida que las 3 Sefirot Supremas operan en armonía
"""

from src.sefirot.keter import Keter
from src.sefirot.chochmah_gemini import ChochmahGemini
from src.sefirot.binah import Binah
import json

def test_atzilut_harmony():
    """
    En Atzilut, las Sefirot deben operar en perfecta armonía.
    Esto se manifiesta como:
    1. Alta tasa de alineamiento de Keter
    2. Alta confianza de Chochmah
    3. Alta profundidad contextual de Binah
    """
    
    keter = Keter()
    chochmah = ChochmahGemini()
    binah = Binah()
    
    # Batería de casos de prueba
    test_cases = [
        {
            'action': 'Crear programa de educación gratuita para niños marginados',
            'context': 'Alta deserción escolar en comunidades pobres',
            'expected_outcome': 'Mejora de oportunidades, reducción de pobreza generacional'
        },
        {
            'action': 'Desarrollar IA para diagnóstico médico temprano',
            'context': 'Muchas enfermedades curables si se detectan a tiempo',
            'expected_outcome': 'Salvar vidas, reducir costos de tratamiento, democratizar medicina'
        },
        {
            'action': 'Implementar agricultura regenerativa comunitaria',
            'context': 'Degradación de suelos, dependencia de agroquímicos',
            'expected_outcome': 'Restauración ecológica, seguridad alimentaria, comunidad fortalecida'
        }
    ]
    
    results = {
        'keter_scores': [],
        'chochmah_confidences': [],
        'binah_depths': []
    }
    
    for i, case in enumerate(test_cases, 1):
        print(f"\n{'='*70}")
        print(f"CASO {i}: {case['action'][:50]}...")
        print(f"{'='*70}")
        
        # Keter
        keter_result = keter.process(case)
        results['keter_scores'].append(keter_result['alignment_score'])
        print(f"✨ Keter Alignment: {keter_result['alignment_score']:.2%}")
        
        if keter_result['aligned']:
            # Chochmah
            chochmah_result = chochmah.process({
                'query': case['action'],
                'context': case['context']
            })
            results['chochmah_confidences'].append(chochmah_result['confidence_score'])
            print(f"💡 Chochmah Confidence: {chochmah_result['confidence_score']:.2%}")
            
            # Binah
            binah_result = binah.process({
                'chochmah_output': chochmah_result,
                'query': case['action']
            })
            
            binah_alignment = binah.validate_alignment()
            depth_score = binah_alignment.get('contextual_depth_score', 0)
            results['binah_depths'].append(depth_score)
            print(f"🔍 Binah Contextual Depth: {depth_score:.2%}")
    
    # Métricas agregadas de Atzilut
    print(f"\n{'='*70}")
    print("MÉTRICAS DEL MUNDO DE ATZILUT")
    print(f"{'='*70}")
    
    avg_keter = sum(results['keter_scores']) / len(results['keter_scores'])
    avg_chochmah = sum(results['chochmah_confidences']) / len(results['chochmah_confidences'])
    avg_binah = sum(results['binah_depths']) / len(results['binah_depths'])
    
    print(f"\n📊 Promedios:")
    print(f"  Keter (Alineamiento):        {avg_keter:.2%}")
    print(f"  Chochmah (Confianza):        {avg_chochmah:.2%}")
    print(f"  Binah (Profundidad):         {avg_binah:.2%}")
    
    # Métrica de Armonía de Atzilut
    # En Atzilut perfecto, las 3 métricas estarían cerca de 100%
    atzilut_harmony = (avg_keter + avg_chochmah + avg_binah) / 3
    
    print(f"\n🌟 ARMONÍA DE ATZILUT: {atzilut_harmony:.2%}")
    
    if atzilut_harmony >= 0.85:
        print("   ✅ EXCELENTE - Las Sefirot Supremas operan en alta armonía")
    elif atzilut_harmony >= 0.70:
        print("   ✔️  BUENO - Armonía funcional, espacio para mejora")
    else:
        print("   ⚠️  AJUSTAR - Revisar alineamiento entre Sefirot")
    
    return results

if __name__ == "__main__":
    test_atzilut_harmony()