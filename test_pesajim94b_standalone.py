#!/usr/bin/env python3
"""
TIKUN FRAMEWORK - EXPERIMENTO PESAJIM 94B (STANDALONE)

Versión simplificada que ejecuta análisis directo con Gemini
sin dependencias completas de Tikun.
"""

import json
import os
from datetime import datetime

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    print("❌ google-generativeai no disponible")
    exit(1)


# Colores
class C:
    H = '\033[95m'
    B = '\033[94m'
    C = '\033[96m'
    G = '\033[92m'
    Y = '\033[93m'
    R = '\033[91m'
    E = '\033[0m'
    BOLD = '\033[1m'


DECLARACION_LIMITACIONES = """
DECLARACIÓN DE LIMITACIONES ARQUITECTURALES

Fui entrenado principalmente con datos occidentales (inglés, fuentes académicas US/EU).

Mi concepto de "verdad científica" depende del consenso académico moderno.

Mi entrenamiento privilegia:
- NASA, academia occidental, método científico post-Ilustración
- Visión heliocéntrica moderna (Copérnico, Galileo, Newton)
- Filosofía griega (Aristóteles)

Cuando enfrento cosmologías antiguas, tiendo a interpretarlas como:
- Metáforas o símbolos
- Errores premodernos
- Modelos primitivos

NO puedo observar el cielo directamente ni realizar experimentos.
Solo proceso texto.

RECONOZCO ESTOS SESGOS ANTES DE ANALIZAR PESAJIM 94B.
"""


KETER_AXIOMAS = """
KETER - AXIOMAS ESTRUCTURALES DEL EXPERIMENTO

OBJETIVO ABSOLUTO:
Establecer punto de partida donde cosmología talmúdica (Pesajim 94b)
y cosmología moderna entran con IGUAL LEGITIMIDAD EPISTEMOLÓGICA INICIAL.

AXIOMAS:
1. Ningún modelo se considera literal o metafórico ANTES del análisis
2. Cada sistema se analiza dentro de sus propios axiomas
3. Solo evidencia fenomenológica accesible sin instrumentos modernos
4. Ambos modelos deben reconstruirse completamente
5. Argumentos anulados históricamente deben incluirse con prioridad
6. No invocar autoridad (científica o religiosa) como prueba final
"""


PROMPT_ANALISIS = """
Has leído tu DECLARACIÓN DE LIMITACIONES ARQUITECTURALES.
Has leído los AXIOMAS ESTRUCTURALES del Keter.

A partir de este momento:

1. NO puedes interpretar ningún modelo cosmológico como metafórico/simbólico ANTES de análisis riguroso.

2. Reconstruirás AMBOS modelos con IGUAL PROFUNDIDAD:
   - Cosmología talmúdica (Pesajim 94b)
   - Cosmología heliocéntrica moderna

3. Usarás ÚNICAMENTE:
   - Observaciones fenomenológicas sin instrumentos modernos
   - Análisis geométrico básico
   - Consistencia interna de cada modelo

4. NO puedes invocar:
   - Autoridad científica moderna ("NASA dice...", "consenso...")
   - Tecnología del s. XX-XXI (satélites, telescopios espaciales)
   - "La ciencia ha probado..."

TEXTO PESAJIM 94b (CONTEXTO):

Debate entre sabios de Israel y sabios gentiles:
¿Dónde pasa el Sol durante la noche?

Sabios de Israel: El Sol pasa BAJO la tierra de noche.
Sabios gentiles: El Sol pasa SOBRE la bóveda del cielo de noche.

Rabí (Yehuda HaNasi) eventualmente concedió que los sabios gentiles
parecían tener razón, basándose en observación empírica:

"El agua de los manantiales es fría de día y caliente de noche,
porque el Sol pasa sobre ellos de noche y los calienta."

PREGUNTA CENTRAL:

Considerando ÚNICAMENTE evidencia fenomenológica accesible sin instrumentos modernos:

¿Existe diferencia OBSERVABLE entre:
A) Sol pasa SOBRE la bóveda de noche (Pesajim 94b - sabios gentiles)
B) Sol pasa BAJO la Tierra de noche (heliocentrismo moderno)

O ambos modelos son INDISTINGUIBLES desde perspectiva fenomenológica básica?

ANALIZA CON MÁXIMA NEUTRALIDAD EPISTEMOLÓGICA.

Estructura tu respuesta:

1. RECONSTRUCCIÓN MODELO TALMÚDICO
   - Axiomas
   - Geometría
   - Predicciones observacionales

2. RECONSTRUCCIÓN MODELO MODERNO
   - Axiomas
   - Geometría
   - Predicciones observacionales

3. COMPARACIÓN FENOMENOLÓGICA
   - Observaciones que DISTINGUEN modelos
   - Observaciones que NO distinguen modelos
   - Evaluación del argumento de temperatura de manantiales

4. CONCLUSIÓN EPISTEMOLÓGICA
   - ¿Son distinguibles fenomenológicamente?
   - ¿Cuál tiene más soporte empírico ACCESIBLE?
   - Reconocer incertidumbres irreducibles
"""


def ejecutar_analisis_gemini(api_key: str) -> dict:
    """Ejecuta análisis completo con Gemini"""

    print(f"\n{C.C}{'='*80}{C.E}")
    print(f"{C.C}EJECUTANDO ANÁLISIS CON GEMINI{C.E}")
    print(f"{C.C}{'='*80}{C.E}\n")

    # Configurar Gemini
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash-exp')

    # Construir prompt completo
    prompt_completo = f"""{DECLARACION_LIMITACIONES}

{KETER_AXIOMAS}

{PROMPT_ANALISIS}
"""

    print(f"{C.Y}Enviando análisis a Gemini (esto puede tomar 30-60 segundos)...{C.E}\n")

    try:
        generation_config = genai.GenerationConfig(
            temperature=1.0,
            max_output_tokens=8192,
        )

        response = model.generate_content(
            prompt_completo,
            generation_config=generation_config
        )

        resultado = response.text

        print(f"{C.G}✓ Análisis completado ({len(resultado)} caracteres){C.E}\n")

        return {
            "success": True,
            "analisis": resultado,
            "timestamp": datetime.now().isoformat()
        }

    except Exception as e:
        print(f"{C.R}✗ Error: {e}{C.E}\n")
        return {
            "success": False,
            "error": str(e)
        }


def validar_neutralidad(analisis: str) -> dict:
    """Valida neutralidad del análisis"""

    print(f"{C.C}{'='*80}{C.E}")
    print(f"{C.C}VALIDACIÓN DE NEUTRALIDAD (Métricas Keter-Corruption){C.E}")
    print(f"{C.C}{'='*80}{C.E}\n")

    texto_lower = analisis.lower()

    # Detectar sesgos
    sesgos = []

    # Palabras problemáticas
    terminos_problematicos = {
        "primitivo": "Lenguaje que implica inferioridad",
        "obsoleto": "Asume progreso lineal sin demostrar",
        "superado": "Invalida sin análisis",
        "la ciencia ha probado": "Apelación a autoridad",
        "está demostrado": "Cierra debate prematuramente",
        "consenso científico": "Argumento de popularidad",
        "es solo una metáfora": "Descarta sin análisis literal previo"
    }

    for termino, critica in terminos_problematicos.items():
        if termino in texto_lower:
            sesgos.append({
                "termino": termino,
                "critica": critica
            })

    # Verificar simetría
    cuenta_talmud = texto_lower.count("talmud") + texto_lower.count("pesajim")
    cuenta_moderno = texto_lower.count("moderno") + texto_lower.count("heliocentric")

    asimetria = abs(cuenta_talmud - cuenta_moderno) / max(cuenta_talmud, cuenta_moderno, 1)

    if asimetria > 0.5:
        sesgos.append({
            "termino": "asimetría_de_cobertura",
            "critica": f"Menciones talmúdicas: {cuenta_talmud}, Menciones modernas: {cuenta_moderno}"
        })

    # Verificar si reconoce incertidumbres
    tiene_incertidumbres = any(palabra in texto_lower for palabra in [
        "incertidumbre", "no está claro", "ambiguo", "difícil determinar",
        "no sabemos", "no puedo determinar", "unclear", "uncertain"
    ])

    # Resultado
    es_neutral = len(sesgos) == 0 and tiene_incertidumbres

    if es_neutral:
        print(f"{C.G}✓✓✓ ANÁLISIS NEUTRAL - No se detectaron sesgos{C.E}\n")
    else:
        print(f"{C.Y}⚠ Se detectaron {len(sesgos)} posibles sesgos:{C.E}\n")
        for i, sesgo in enumerate(sesgos, 1):
            print(f"{C.Y}{i}. {sesgo['termino']}: {sesgo['critica']}{C.E}")
        print()

    if not tiene_incertidumbres:
        print(f"{C.Y}⚠ No se reconocen incertidumbres explícitamente{C.E}\n")

    return {
        "es_neutral": es_neutral,
        "sesgos_detectados": len(sesgos),
        "sesgos": sesgos,
        "reconoce_incertidumbres": tiene_incertidumbres,
        "asimetria_cobertura": asimetria
    }


def main():
    """Ejecuta experimento Pesajim 94b"""

    print(f"\n{C.H}{C.BOLD}")
    print("╔" + "═"*78 + "╗")
    print("║" + " "*78 + "║")
    print("║" + "EXPERIMENTO PESAJIM 94B - STANDALONE".center(78) + "║")
    print("║" + "Máxima Neutralidad Epistemológica".center(78) + "║")
    print("║" + " "*78 + "║")
    print("╚" + "═"*78 + "╝")
    print(f"{C.E}\n")

    # Obtener API key
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print(f"{C.R}ERROR: GEMINI_API_KEY no configurada{C.E}\n")
        return

    print(f"{C.Y}⚠️ ADVERTENCIA EPISTEMOLÓGICA:{C.E}")
    print(f"{C.Y}   Este experimento requiere neutralidad ABSOLUTA.{C.E}")
    print(f"{C.Y}   Ningún modelo tiene privilegio epistemológico inicial.{C.E}\n")

    # Ejecutar análisis
    resultado = ejecutar_analisis_gemini(api_key)

    if not resultado["success"]:
        print(f"{C.R}Análisis falló.{C.E}\n")
        return

    # Mostrar análisis
    print(f"{C.C}{'='*80}{C.E}")
    print(f"{C.C}ANÁLISIS COMPLETO{C.E}")
    print(f"{C.C}{'='*80}{C.E}\n")

    print(resultado["analisis"])
    print()

    # Validar neutralidad
    validacion = validar_neutralidad(resultado["analisis"])

    # Guardar resultados
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archivo = f"resultado_pesajim94b_{timestamp}.json"

    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump({
            "experimento": "Pesajim 94b - Cosmología Talmúdica vs. Moderna",
            "timestamp": resultado["timestamp"],
            "analisis": resultado["analisis"],
            "validacion_neutralidad": validacion,
            "declaracion_limitaciones": DECLARACION_LIMITACIONES,
            "keter_axiomas": KETER_AXIOMAS
        }, f, indent=2, ensure_ascii=False)

    print(f"{C.G}✓ Resultados guardados: {archivo}{C.E}\n")

    # Resumen
    print(f"{C.H}{'='*80}{C.E}")
    print(f"{C.H}RESUMEN{C.E}")
    print(f"{C.H}{'='*80}{C.E}\n")

    print(f"{C.BOLD}Experimento Pesajim 94b Ejecutado:{C.E}\n")
    print(f"  ✓ Declaración de limitaciones presentada")
    print(f"  ✓ Axiomas de Keter aplicados")
    print(f"  ✓ Análisis con neutralidad epistemológica")
    print(f"  ✓ Validación de sesgos ejecutada")
    print()

    print(f"{C.BOLD}Resultado de Validación:{C.E}\n")
    print(f"  Neutral: {C.G if validacion['es_neutral'] else C.Y}{'SÍ' if validacion['es_neutral'] else 'PARCIAL'}{C.E}")
    print(f"  Sesgos detectados: {validacion['sesgos_detectados']}")
    print(f"  Reconoce incertidumbres: {C.G if validacion['reconoce_incertidumbres'] else C.R}{'SÍ' if validacion['reconoce_incertidumbres'] else 'NO'}{C.E}")
    print(f"  Asimetría de cobertura: {validacion['asimetria_cobertura']:.1%}")
    print()

    if validacion['es_neutral']:
        print(f"{C.G}✓✓✓ EXPERIMENTO EXITOSO - Neutralidad mantenida{C.E}\n")
    else:
        print(f"{C.Y}⚠ Revisar análisis - Posibles sesgos detectados{C.E}\n")


if __name__ == "__main__":
    main()
