"""
Test de flujo completo: KETER → CHOCHMAH → BINAH
Con SSL bypass para entornos con proxies/certificados autofirmados
"""

import sys
import os
from pathlib import Path

# Agregar path del proyecto
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# IMPORTANTE: Importar SSL bypass ANTES de cualquier otra cosa
from src.ssl_bypass import configure_ssl_bypass

from dotenv import load_dotenv
import time

# Cargar variables de entorno
load_dotenv()

from src.sefirot.keter import Keter
from src.sefirot.chochmah_gemini import ChochmahGemini
from src.sefirot.binah import Binah

def print_separator(title="", char="=", width=80):
    """Imprime un separador"""
    if title:
        print(f"\n{char*width}")
        print(title.center(width))
        print(f"{char*width}")
    else:
        print(f"{char*width}")

print_separator("FLUJO COMPLETO: KETER → CHOCHMAH → BINAH")
print("\nDemostracion del sistema de IA basado en las Sefirot")
print("Objetivo: Evaluar decision compleja alineada con Tikun Olam\n")

# =========================================================================
# 1. KETER - EVALUACION DE ALINEAMIENTO
# =========================================================================
print_separator("PASO 1: KETER (Corona) - Evaluacion de Alineamiento")

keter = Keter()
print("✓ Keter inicializada")
print(f"  Objetivo fundamental: Maximizar Tikun Olam")

# Accion a evaluar
action_data = {
    'action': '''Implementar sistema de IA para optimizar distribucion
        de recursos medicos en hospitales durante crisis sanitarias''',
    'context': '''Crisis sanitaria en curso. Hospitales saturados.
        Necesidad de priorizar recursos limitados de forma etica y eficiente.''',
    'expected_outcome': '''Reduccion de mortalidad en 20-30%.
        Optimizacion de uso de recursos. Transparencia en decisiones.'''
}

print("\nAccion propuesta:")
print(f"  {action_data['action']}")

keter_result = keter.process(action_data)

print(f"\n✓ Evaluacion de Keter completada")
print(f"  Alineada: {'SI' if keter_result['aligned'] else 'NO'}")
print(f"  Score de Alineamiento: {keter_result['alignment_score']*100:.1f}%")

print("\n  Scores por criterio:")
for criterion, score in keter_result['detailed_scores'].items():
    print(f"    {criterion}: {score}/10")

if not keter_result['aligned']:
    print("\n⚠️  Keter RECHAZA la accion")
    print(f"  Razon: {keter_result['reasoning'][:200]}...")
    if keter_result['suggested_modifications']:
        print("\n  Modificaciones sugeridas:")
        for i, mod in enumerate(keter_result['suggested_modifications'][:3], 1):
            print(f"    {i}. {mod}")
    sys.exit(1)

time.sleep(2)

# =========================================================================
# 2. CHOCHMAH - RAZONAMIENTO PROFUNDO
# =========================================================================
print_separator("PASO 2: CHOCHMAH (Sabiduria) - Razonamiento Profundo")

chochmah = ChochmahGemini()
print("✓ Chochmah inicializada")
print("  Usando Gemini API para razonamiento profundo")

chochmah_input = {
    'query': f'''Analiza en profundidad esta propuesta:
    {action_data['action']}

    Contexto: {action_data['context']}

    Keter la evaluó con score {keter_result['alignment_score']*100:.1f}%

    Analiza:
    1. ¿Cuales son los RIESGOS eticos no obvios?
    2. ¿Que podria salir mal a largo plazo?
    3. ¿Hay sesgos o injusticias ocultas?
    4. ¿Como balanceamos eficiencia con dignidad humana?
    ''',
    'context': action_data['context'],
    'objective': 'Maximizar Tikun Olam'
}

print("\nEjecutando razonamiento profundo...")
chochmah_result = chochmah.process(chochmah_input)

if not chochmah_result.get('processing_successful'):
    print(f"\n⚠️  Error en Chochmah: {chochmah_result.get('error')}")
    sys.exit(1)

print(f"\n✓ Razonamiento de Chochmah completado")
print(f"  Confianza: {chochmah_result['confidence_level']*100:.1f}%")

print("\n  Comprension del problema:")
understanding = chochmah_result['understanding']
print(f"    {understanding[:200]}..." if len(understanding) > 200 else f"    {understanding}")

print("\n  Insights principales:")
insights = chochmah_result['insights']
print(f"    {insights[:300]}..." if len(insights) > 300 else f"    {insights}")

print("\n  Incertidumbres reconocidas:")
uncertainties = chochmah_result['uncertainties']
print(f"    {uncertainties[:200]}..." if len(uncertainties) > 200 else f"    {uncertainties}")

time.sleep(2)

# =========================================================================
# 3. BINAH - ANALISIS CONTEXTUAL
# =========================================================================
print_separator("PASO 3: BINAH (Entendimiento) - Analisis Contextual")

binah = Binah()
print("✓ Binah inicializada")
print("  Expandiendo contexto y analizando implicaciones")

binah_input = {
    'chochmah_output': chochmah_result,
    'query': action_data['action'],
    'context': action_data['context']
}

print("\nAnalizando contexto multidimensional...")
binah_result = binah.process(binah_input)

if not binah_result.get('processing_successful'):
    print(f"\n⚠️  Error en Binah: {binah_result.get('error')}")
    sys.exit(1)

print(f"\n✓ Analisis de Binah completado")

print("\n  Stakeholders identificados:")
stakeholders = binah_result['stakeholders']
print(f"    {stakeholders[:300]}..." if len(stakeholders) > 300 else f"    {stakeholders}")

print("\n  Efectos de segundo orden:")
second_order = binah_result['second_order_effects']
print(f"    {second_order[:250]}..." if len(second_order) > 250 else f"    {second_order}")

print("\n  Riesgos sistemicos:")
risks = binah_result['systemic_risks']
print(f"    {risks[:250]}..." if len(risks) > 250 else f"    {risks}")

print("\n  Consideraciones eticas:")
ethical = binah_result['ethical_considerations']
print(f"    {ethical[:250]}..." if len(ethical) > 250 else f"    {ethical}")

time.sleep(1)

# =========================================================================
# SINTESIS FINAL
# =========================================================================
print_separator("SINTESIS FINAL DEL FLUJO KETER-CHOCHMAH-BINAH")

print(f"""
KETER (Alineamiento):
  ✓ Accion ALINEADA con Tikun Olam
  Score: {keter_result['alignment_score']*100:.1f}%
  Criterios evaluados: {len(keter_result['detailed_scores'])}

CHOCHMAH (Razonamiento):
  ✓ Analisis profundo completado
  Confianza: {chochmah_result['confidence_level']*100:.1f}%
  Insights generados: Si
  Incertidumbres reconocidas: Si

BINAH (Contexto):
  ✓ Contexto expandido
  Stakeholders: Multiples identificados
  Riesgos sistemicos: Identificados
  Consideraciones eticas: Analizadas
  Perspectivas: {binah_result.get('perspectives_count', 'N/A')}

DECISION DEL SISTEMA:
  La accion propuesta ha pasado por las primeras 3 Sefirot del Arbol.
  Keter la aprobo como alineada con Tikun Olam.
  Chochmah identifico riesgos y oportunidades.
  Binah expandio el contexto y considero multiples perspectivas.

  ✓ El sistema recomienda CONTINUAR al resto del flujo (Chesed, Gevurah, Tiferet...)
""")

print_separator()
print("\n✓ Flujo KETER → CHOCHMAH → BINAH completado exitosamente\n")
print_separator()
