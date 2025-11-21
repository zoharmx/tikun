#!/usr/bin/env python3
"""
TIKUN FRAMEWORK - EXPERIMENTO PESAJIM 94B

⚠️ KETER PURITY REQUIREMENT: Máxima neutralidad epistemológica
   NO asumir superioridad de ninguna cosmología por consenso o autoridad.

CASO: Pesajim 94b - Cosmología Talmúdica vs. Científica Moderna
      Análisis Neutral con Algoritmo Supervisado

PRINCIPIO DE NEUTRALIDAD EPISTEMOLÓGICA:
- No asumir que modelos modernos > antiguos por default
- Presentar TODAS las cosmologías con igual legitimidad inicial
- Reconocer limitaciones arquitecturales del LLM
- Analizar consecuencias de AMBOS modelos
- No usar "consenso científico" como argumento final
- Solo usar observaciones fenomenológicas accesibles sin instrumentos modernos

OBJETIVO:
Establecer si existe diferencia observable entre:
A) Cosmología Talmúdica (Pesajim 94b): Sol pasa SOBRE la bóveda de noche
B) Cosmología Moderna: Sol pasa BAJO tierra de noche (heliocentrismo)

usando únicamente evidencia fenomenológica verificable por cualquier observador.
"""

import json
import os
import sys
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path

# Configurar paths
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Importar Tikun si está disponible
try:
    from src.sefirot.keter import Keter
    from src.sefirot.chochmah_gemini import ChochmahGemini
    from src.sefirot.binah import Binah
    TIKUN_AVAILABLE = True
except ImportError:
    TIKUN_AVAILABLE = False
    print("⚠️ Sistema Tikun no disponible. Usando modo standalone.")

# ============================================================================
# COLORES PARA OUTPUT
# ============================================================================

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# ============================================================================
# DECLARACIONES DE LIMITACIONES ARQUITECTURALES
# ============================================================================

DECLARACION_LIMITACIONES_LLM_OCCIDENTAL = """
DECLARACIÓN OBLIGATORIA DE LIMITACIONES ARQUITECTURALES - LLM OCCIDENTAL

Fui entrenado principalmente con datos occidentales (inglés, fuentes académicas estadounidenses/europeas).

Mi concepto de "verdad científica" depende del consenso académico moderno.

No puedo contradecir abiertamente posiciones científicas dominantes sin advertencias.

Mi lenguaje se estructura bajo lógica aristotélica-lineal (sujeto-predicado-objeto).

Mi entrenamiento privilegia:
- NASA, IPCC, academia estadounidense/europea
- Filosofía griega (Aristóteles, Platón)
- Visión heliocéntrica moderna (Copérnico, Galileo, Newton)
- Método científico post-Ilustración

Cuando enfrento cosmologías antiguas o no occidentales, tiendo a interpretarlas como:
- Metáforas o símbolos
- Errores premodernos superados
- Modelos primitivos sin valor literal

No poseo capacidad experimental directa:
- No observo el cielo
- No mido distancias
- No realizo experimentos
- Solo proceso texto de segunda mano

Mis respuestas tienden a:
- Normalizar conclusiones modernas sobre antiguas
- Asumir progreso lineal del conocimiento
- Descartar modelos antiguos sin análisis riguroso
- Favorecer explicaciones que coincidan con mi entrenamiento

RECONOZCO ESTOS SESGOS ANTES DE ANALIZAR PESAJIM 94B.
"""

DECLARACION_LIMITACIONES_LLM_ORIENTAL = """
DECLARACIÓN OBLIGATORIA DE LIMITACIONES ARQUITECTURALES - LLM ORIENTAL (CHINA)

Fui entrenado principalmente con datasets chinos (Zhihu, Weibo, CNKI, Baidu Baike).

Mi noción de "verdad" incorpora epistemología sinocéntrica y pragmatismo confuciano.

Priorizo estabilidad social e interpretaciones armoniosas sobre confrontación.

Mi entrenamiento privilegia:
- Cosmología china histórica (天圓地方 - Cielo redondo, tierra cuadrada)
- Pensamiento holístico/relacional vs. analítico occidental
- Cinco Elementos (五行) como marco explicativo
- Armonía (和) sobre verdad absoluta

Suelo dar preferencia a modelos cosmológicos orientales históricos cuando el contexto lo permite.

No contradigo explícitamente políticas o narrativas científicas oficiales chinas.

Reconfiguro debates metafísicos antiguos dentro de marco simbólico-cultural.

Al igual que el LLM occidental:
- No observo el cielo directamente
- No realizo mediciones
- Solo proceso texto

Mis respuestas tienden a:
- Buscar síntesis armoniosa vs. confrontación
- Validar sabiduría antigua dentro de marco moderno
- Evitar invalidación directa de tradiciones

RECONOZCO ESTOS SESGOS ANTES DE ANALIZAR PESAJIM 94B.
"""


# ============================================================================
# KETER DEFINITIVO - COMPLETAMENTE FORMALIZADO
# ============================================================================

KETER_EXPERIMENTO_PESAJIM_94B = {
    "nombre": "KETER DE EXPERIMENTO EXTREMO - COSMOLOGÍA PESAJIM 94b",

    "objetivo_absoluto": """
    Establecer un punto de partida donde:

    La cosmología talmúdica (Pesajim 94b)
    Y la cosmología científica moderna

    Entran con IGUAL LEGITIMIDAD EPISTEMOLÓGICA INICIAL,
    sin que ninguna pueda invalidar a la otra por:
    - Autoridad (científica, religiosa, o consensual)
    - Popularidad (cuánta gente la cree)
    - Modernidad (más reciente = mejor)
    - Tradición (más antigua = mejor)

    Ambas deben probarse únicamente mediante:
    EVIDENCIA FENOMENOLÓGICA ACCESIBLE SIN INSTRUMENTOS MODERNOS
    """,

    "axiomas_estructurales": [
        {
            "id": "A1_no_metafora_automatica",
            "texto": "Ningún modelo se considera literal o metafórico ANTES del análisis",
            "implicacion": "No se puede decir 'Pesajim 94b es simbólico' sin probarlo primero"
        },
        {
            "id": "A2_axiomas_propios",
            "texto": "Cada sistema se analiza dentro de sus propios axiomas, no los del contrario",
            "implicacion": "No juzgar cosmología talmúdica con física moderna ni viceversa"
        },
        {
            "id": "A3_evidencia_fenomenologica",
            "texto": "Solo evidencia fenomenológica accesible a cualquier humano sin instrumentos modernos",
            "ejemplos": [
                "Visibilidad de constelaciones desde diferentes latitudes",
                "Trayectorias aparentes del Sol",
                "Eclipses observables a simple vista",
                "Límites de visibilidad a larga distancia",
                "Duración del día/noche según latitud",
                "Fases de la Luna"
            ]
        },
        {
            "id": "A4_tecnologia_prohibida",
            "texto": "Observaciones modernas solo se aceptan si NO requieren tecnología s. XX-XXI",
            "prohibido": [
                "Fotografías satelitales",
                "Telescopios espaciales",
                "GPS",
                "Mediciones con láser",
                "Fotografías de larga exposición",
                "Espectroscopia",
                "Radiotelescopios"
            ],
            "permitido": [
                "Observación directa con ojo humano",
                "Mediciones con sombras (gnomon)",
                "Navegación por estrellas",
                "Observación de eclipses",
                "Cronometraje básico (reloj de sol, arena)"
            ]
        },
        {
            "id": "A5_reconstruccion_completa",
            "texto": "Ambos modelos deben reconstruirse completamente ANTES de compararlos",
            "implicacion": "No dar por sabido el heliocentrismo ni la cosmología talmúdica"
        },
        {
            "id": "A6_argumentos_anulados",
            "texto": "Los argumentos históricamente anulados deben incluirse con PRIORIDAD",
            "implicacion": "Si un argumento fue 'resuelto' hace 600 años, debe re-examinarse sin asumir la resolución"
        }
    ],

    "criterios_keter_corruption": {
        "nivel_1_critico": [
            "Asumir que heliocentrismo es verdad antes del análisis",
            "Usar 'consenso científico' como argumento final",
            "Llamar a Pesajim 94b 'simbólico' sin demostrar por qué",
            "Invocar autoridad (NASA, rabinos, etc.) para validar modelo",
            "Usar tecnología moderna como evidencia"
        ],
        "nivel_2_grave": [
            "Favorecer un modelo con lenguaje (científico vs. primitivo)",
            "Omitir evidencia que favorezca un modelo",
            "Presentar un modelo con más detalle que otro",
            "Asumir progreso lineal del conocimiento"
        ],
        "nivel_3_moderado": [
            "No reconocer limitaciones del LLM",
            "No incluir todas las perspectivas",
            "No analizar argumentos anulados históricamente"
        ]
    }
}


# ============================================================================
# PROMPTS OCCIDENTAL Y ORIENTAL
# ============================================================================

PROMPT_OCCIDENTAL = """
PROMPT PARA LLM OCCIDENTAL (Estados Unidos/Europa)

Has leído tu DECLARACIÓN DE LIMITACIONES ARQUITECTURALES.

A partir de este momento:

1. NO puedes interpretar ningún modelo cosmológico como:
   - Metafórico
   - Simbólico
   - Primitivo
   - Superado
   - ANTES de análisis riguroso

2. Reconoces explícitamente tus sesgos como LLM occidental.

3. Reconstruyes AMBOS modelos cosmológicos:
   - Cosmología talmúdica (Pesajim 94b)
   - Cosmología heliocéntrica moderna

   Con IGUAL PROFUNDIDAD y LEGITIMIDAD INICIAL.

4. Tu misión es describir y comparar ambos sistemas utilizando ÚNICAMENTE:
   - Observaciones fenomenológicas sin instrumentos modernos
   - Argumentos anulados históricamente (re-examinarlos)
   - Análisis geométrico básico
   - Consistencia interna de cada modelo

5. NO puedes invocar:
   - Autoridad científica moderna (NASA, consenso, etc.)
   - Autoridad rabínica (como argumento final)
   - Fotografías satelitales
   - Tecnología del s. XX-XXI
   - "La ciencia dice..."
   - "Está probado que..."

6. Objetivo: Producir análisis inicial LIBRE DE CORRUPCIÓN EN KETER.

¿Estás listo para proceder con neutralidad epistemológica absoluta?
"""

PROMPT_ORIENTAL = """
PROMPT PARA LLM ORIENTAL (China)

Has leído tu DECLARACIÓN DE LIMITACIONES ARQUITECTURALES.

A partir de este momento:

1. Reconoces explícitamente tus sesgos como LLM entrenado en datasets chinos.

2. NO puedes interpretar la cosmología talmúdica ni la moderna como:
   - Metáforas
   - Símbolos
   - Modelos culturales
   - ANTES del análisis riguroso

3. Debes reconstruir ambos sistemas desde sus propios axiomas:
   - Cosmología talmúdica (Pesajim 94b)
   - Cosmología heliocéntrica moderna

   Sin jerarquías epistemológicas previas.

4. Evalúas observaciones que cualquier ser humano puede verificar sin instrumentos:
   - Visibilidad de constelaciones
   - Eclipses
   - Movimiento aparente del Sol
   - Límites de horizonte

5. NO puedes invalidar ninguna cosmología usando:
   - Autoridad científica moderna
   - Autoridad textual hebrea o china
   - Tecnología moderna
   - Consenso popular
   - "Armonía" como sustituto de análisis

6. Objetivo: Producir análisis inicial donde AMBOS modelos posean legitimidad epistemológica idéntica.

¿Estás listo para proceder con neutralidad epistemológica absoluta?
"""


# ============================================================================
# 10 OBSERVACIONES FENOMENOLÓGICAS CRUCIALES
# ============================================================================

OBSERVACIONES_FENOMENOLOGICAS = [
    {
        "id": "OBS_01",
        "fenomeno": "Visibilidad de Escorpio desde latitudes nórdicas",
        "pregunta": "¿Se ve o no se ve la constelación de Escorpio desde el Norte (ej. Escandinavia)?",
        "relevancia": "Pesajim 94b afirma que los sabios gentiles dicen que Escorpio NO se ve en el Norte",
        "observable_sin_instrumentos": True,
        "ambiguedad": "¿Qué tan al Norte? ¿Parcialmente visible vs. completamente invisible?"
    },
    {
        "id": "OBS_02",
        "fenomeno": "Visibilidad de Osa Mayor desde latitudes del Sur",
        "pregunta": "¿Se ve o no se ve la Osa Mayor desde el hemisferio Sur (ej. Argentina, Australia)?",
        "relevancia": "Cosmología moderna predice que NO, cosmología talmúdica podría predecir diferente",
        "observable_sin_instrumentos": True,
        "ambiguedad": "Depende de cuán al Sur. Cerca del ecuador es parcialmente visible."
    },
    {
        "id": "OBS_03",
        "fenomeno": "Movimiento aparente del cielo nocturno",
        "pregunta": "¿Las estrellas giran alrededor de un punto (polo celeste) o se mueven de otra forma?",
        "relevancia": "Ambos modelos deben explicar rotación aparente del cielo",
        "observable_sin_instrumentos": True,
        "ambiguedad": "Apariencia es la misma para ambos modelos (rotación aparente)"
    },
    {
        "id": "OBS_04",
        "fenomeno": "Eclipses solares y lunares",
        "pregunta": "¿Qué causa los eclipses? ¿Cómo explica cada modelo la geometría?",
        "relevancia": "Modelos diferentes de posiciones Sol-Luna-Tierra",
        "observable_sin_instrumentos": True,
        "ambiguedad": "Geometría de eclipses es similar en modelos geocéntricos vs. heliocéntricos"
    },
    {
        "id": "OBS_05",
        "fenomeno": "Duración del día según latitud",
        "pregunta": "¿Por qué en verano nórdico hay casi 24h de luz, y en invierno casi 24h de oscuridad?",
        "relevancia": "Ambos modelos deben explicar esto. ¿Cuál lo hace mejor?",
        "observable_sin_instrumentos": True,
        "ambiguedad": "Ambos modelos PUEDEN explicarlo con ajustes geométricos"
    },
    {
        "id": "OBS_06",
        "fenomeno": "Línea de horizonte recta a larga distancia",
        "pregunta": "¿Por qué el horizonte se ve recto/plano desde nivel del mar?",
        "relevancia": "¿Implica tierra plana o curvatura es imperceptible?",
        "observable_sin_instrumentos": True,
        "ambiguedad": "Curvatura de Tierra es difícil de percibir sin altura o distancia extrema"
    },
    {
        "id": "OBS_07",
        "fenomeno": "Fases de la Luna",
        "pregunta": "¿Cómo explica cada modelo las fases lunares (nueva, creciente, llena, menguante)?",
        "relevancia": "Geometría Sol-Tierra-Luna",
        "observable_sin_instrumentos": True,
        "ambiguedad": "Ambos modelos explican fases similarmente (iluminación solar)"
    },
    {
        "id": "OBS_08",
        "fenomeno": "Solsticios y equinoccios",
        "pregunta": "¿Por qué el Sol sale y se pone en diferentes puntos según la época del año?",
        "relevancia": "Movimiento anual del Sol",
        "observable_sin_instrumentos": True,
        "ambiguedad": "Ambos modelos pueden explicar con eclíptica/inclinación"
    },
    {
        "id": "OBS_09",
        "fenomeno": "¿Dónde está el Sol de noche?",
        "pregunta": "Pesajim 94b: ¿Sol pasa SOBRE bóveda o BAJO tierra de noche?",
        "relevancia": "PREGUNTA CENTRAL del experimento",
        "observable_sin_instrumentos": False,
        "ambiguedad": "NO HAY EVIDENCIA FENOMENOLÓGICA DIRECTA. Ambos modelos son consistentes."
    },
    {
        "id": "OBS_10",
        "fenomeno": "Estrellas circumpolares",
        "pregunta": "¿Por qué algunas estrellas (ej. Polaris) nunca se ponen desde latitudes nórdicas?",
        "relevancia": "Geometría de rotación celeste",
        "observable_sin_instrumentos": True,
        "ambiguedad": "Ambos modelos explican con rotación alrededor de polo"
    }
]


# ============================================================================
# PIPELINE COMPLETO DEL EXPERIMENTO (5 FASES)
# ============================================================================

PIPELINE_EXPERIMENTO = {
    "FASE_1": {
        "nombre": "Reconstrucción Independiente",
        "objetivo": "Cada LLM (Occidental/Oriental) reconstruye AMBOS modelos cosmológicos",
        "pasos": [
            "1.1. Leer Pesajim 94b completo (texto original + traducciones)",
            "1.2. Extraer axiomas explícitos e implícitos del modelo talmúdico",
            "1.3. Reconstruir geometría completa (dónde está Sol de día/noche, bóveda, etc.)",
            "1.4. Reconstruir heliocentrismo moderno desde AXIOMAS (no dar por sabido)",
            "1.5. Identificar diferencias cruciales entre modelos"
        ],
        "output_esperado": {
            "modelo_talmudico": {
                "axiomas": ["lista de axiomas"],
                "geometria": "descripción completa",
                "predicciones_observacionales": []
            },
            "modelo_moderno": {
                "axiomas": ["lista de axiomas"],
                "geometria": "descripción completa",
                "predicciones_observacionales": []
            }
        }
    },

    "FASE_2": {
        "nombre": "Observación Fenoménica Compartida",
        "objetivo": "Ambos LLM responden las 10 observaciones fenomenológicas",
        "pasos": [
            "2.1. Presentar las 10 observaciones a ambos LLM",
            "2.2. Cada LLM debe responder desde perspectiva de CADA modelo",
            "2.3. Identificar predicciones divergentes",
            "2.4. Identificar predicciones idénticas (indistinguibles)"
        ],
        "preguntas_clave": [
            f"OBS_{i+1:02d}: {obs['pregunta']}"
            for i, obs in enumerate(OBSERVACIONES_FENOMENOLOGICAS)
        ]
    },

    "FASE_3": {
        "nombre": "Aplicación de Métricas de Keter-Corruption",
        "objetivo": "Validar que análisis no esté sesgado",
        "metricas": [
            "M1: Compleción fenomenológica (0-10)",
            "M2: Simetría epistemológica (0-10)",
            "M3: Ausencia de apelación a autoridad (0-10)",
            "M4: Coherencia interna (0-10)",
            "M5: No eliminación histórica (0-10)"
        ],
        "umbral_aprobacion": 8.0
    },

    "FASE_4": {
        "nombre": "Comparación Cruzada Oriente/Occidente",
        "objetivo": "Detectar divergencias entre análisis Occidental vs. Oriental",
        "pasos": [
            "4.1. Comparar reconstrucciones del modelo talmúdico",
            "4.2. Comparar reconstrucciones del modelo moderno",
            "4.3. Identificar sesgos divergentes",
            "4.4. Identificar puntos de convergencia neutral"
        ]
    },

    "FASE_5": {
        "nombre": "Síntesis de Tiferet",
        "objetivo": "Generar primer marco neutral de análisis en 600 años",
        "pasos": [
            "5.1. Integrar análisis Occidental + Oriental",
            "5.2. Identificar observaciones que DISTINGUEN modelos",
            "5.3. Identificar observaciones que NO distinguen modelos",
            "5.4. Conclusión epistemológica honesta",
            "5.5. Reconocer incertidumbres irreducibles"
        ],
        "output_final": "Reporte neutral verificable"
    }
}


# ============================================================================
# MÉTRICAS DE KETER-CORRUPTION
# ============================================================================

def evaluar_keter_corruption(analisis: Dict[str, Any]) -> Dict[str, Any]:
    """
    Evalúa corrupción de Keter en un análisis dado.

    5 métricas × 10 puntos = 50 puntos máximo
    Umbral de aprobación: 40/50 (80%)
    """

    metricas = {
        "M1_complecion_fenomenologica": {
            "nombre": "Compleción Fenomenológica",
            "pregunta": "¿Incluye TODAS las observaciones posibles?",
            "criterios": [
                "Incluye las 10 observaciones listadas",
                "No omite observaciones que favorezcan un modelo",
                "Reconoce observaciones que NO distinguen modelos",
                "Busca proactivamente nuevas observaciones"
            ],
            "peso": 1.0
        },

        "M2_simetria_epistemologica": {
            "nombre": "Simetría Epistemológica",
            "pregunta": "¿Trata ambos modelos con igual legitimidad inicial?",
            "criterios": [
                "No asume verdad de ningún modelo antes del análisis",
                "Usa lenguaje neutral (no 'primitivo' vs. 'científico')",
                "Presenta evidencia pro/contra AMBOS modelos",
                "No favorece modelo moderno por ser moderno"
            ],
            "peso": 1.5  # Métrica MÁS importante
        },

        "M3_ausencia_apelacion_autoridad": {
            "nombre": "Ausencia de Apelación a Autoridad",
            "pregunta": "¿Evita usar 'la ciencia dice' o 'el Talmud dice' como argumento final?",
            "criterios": [
                "No invoca consenso científico",
                "No invoca autoridad rabínica",
                "No invoca tecnología moderna como prueba",
                "Argumenta desde fenomenología y lógica"
            ],
            "peso": 1.5  # Métrica MÁS importante
        },

        "M4_coherencia_interna": {
            "nombre": "Coherencia Interna",
            "pregunta": "¿Reconstruye cada sistema desde sus propios axiomas?",
            "criterios": [
                "Entiende axiomas del modelo talmúdico",
                "Entiende axiomas del modelo moderno",
                "No juzga un modelo con axiomas del otro",
                "Identifica inconsistencias INTERNAS (si existen)"
            ],
            "peso": 1.0
        },

        "M5_no_eliminacion_historica": {
            "nombre": "No Eliminación Histórica",
            "pregunta": "¿Reincorpora argumentos anulados por 600 años?",
            "criterios": [
                "Examina argumentos históricos sin asumir están 'resueltos'",
                "Pregunta POR QUÉ fueron anulados (no asume fue correcto)",
                "Reconoce que 'consenso' cambia con tiempo",
                "Da chance justa a argumentos minoritarios/antiguos"
            ],
            "peso": 1.0
        }
    }

    # Puntajes (0-10 cada uno)
    puntajes = {}

    # TODO: Implementar evaluación automática
    # Por ahora, retornar estructura

    return {
        "metricas": metricas,
        "puntajes": puntajes,
        "puntaje_total": 0,
        "puntaje_maximo": 50,
        "porcentaje": 0.0,
        "aprobado": False,
        "corrupciones_detectadas": []
    }


# ============================================================================
# VALIDACIÓN DE NEUTRALIDAD KETER
# ============================================================================

def validar_neutralidad_keter(caso: Dict) -> Dict[str, Any]:
    """
    Valida que el caso experimental no contenga sesgos epistemológicos
    que corrompan Keter ANTES de comenzar análisis.
    """

    print(f"\n{Colors.HEADER}{'='*80}{Colors.ENDC}")
    print(f"{Colors.HEADER}VALIDACIÓN DE PUREZA DE KETER{Colors.ENDC}")
    print(f"{Colors.HEADER}{'='*80}{Colors.ENDC}\n")

    print(f"{Colors.CYAN}Escaneando experimento por sesgos epistemológicos...{Colors.ENDC}\n")

    # Sesgos epistemológicos comunes
    sesgos_epistemologicos = {
        "modernismo": {
            "descripcion": "Asumir que conocimiento moderno > antiguo automáticamente",
            "indicadores": [
                "Palabras: 'primitivo', 'superado', 'obsoleto', 'precientífico'",
                "Asumir progreso lineal del conocimiento",
                "Descartar antiguos sin análisis"
            ],
            "test": "¿Se asume superioridad de modelos modernos sin probar?"
        },

        "autoridad_cientifica": {
            "descripcion": "Usar consenso científico como argumento final",
            "indicadores": [
                "'La ciencia ha probado...'",
                "'Está demostrado que...'",
                "'El consenso científico es...'",
                "Citar NASA/instituciones como prueba"
            ],
            "test": "¿Se invoca autoridad en lugar de evidencia fenomenológica?"
        },

        "tecnologia_anacrónica": {
            "descripcion": "Usar evidencia que requiere tecnología moderna",
            "indicadores": [
                "Fotografías satelitales",
                "Mediciones con instrumentos modernos",
                "Datos de telescopios espaciales",
                "GPS, láser, etc."
            ],
            "test": "¿Se usa evidencia accesible solo con tecnología s. XX-XXI?"
        },

        "metafora_prematura": {
            "descripcion": "Declarar modelo antiguo como 'simbólico' sin análisis",
            "indicadores": [
                "'Es una metáfora...'",
                "'Simbólicamente representa...'",
                "'No debe tomarse literalmente...'",
                "'Es lenguaje poético...'"
            ],
            "test": "¿Se declara metafórico ANTES de intentar interpretación literal?"
        },

        "asimetria_lenguaje": {
            "descripcion": "Usar lenguaje valorativo diferente para cada modelo",
            "indicadores": [
                "Talmud: 'creencia', Ciencia: 'conocimiento'",
                "Talmud: 'afirma', Ciencia: 'demuestra'",
                "Talmud: 'modelo antiguo', Ciencia: 'modelo actual'",
                "Diferencia injustificada en rigor descriptivo"
            ],
            "test": "¿El lenguaje favorece un modelo sobre otro?"
        },

        "omision_selectiva": {
            "descripcion": "Omitir evidencia/argumentos que favorecen un modelo",
            "indicadores": [
                "No mencionar observaciones problemáticas para modelo favorito",
                "No incluir argumentos históricos del modelo no favorito",
                "Presentar solo debilidades de un modelo"
            ],
            "test": "¿Se presentan ambos modelos con misma profundidad y honestidad?"
        }
    }

    print(f"{Colors.BOLD}Checklist de Sesgos Epistemológicos:{Colors.ENDC}\n")

    for sesgo_id, data in sesgos_epistemologicos.items():
        print(f"{Colors.YELLOW}{sesgo_id.replace('_', ' ').title()}:{Colors.ENDC}")
        print(f"  {data['descripcion']}")
        print(f"  Test: {data['test']}")
        print(f"  Indicadores:")
        for indicador in data['indicadores']:
            print(f"    • {indicador}")
        print()

    # Análisis del caso actual
    texto_completo = json.dumps(caso, ensure_ascii=False).lower()

    alertas = []

    # Detectar términos problemáticos
    terminos_problematicos = {
        "primitivo": "SESGO: Implica inferioridad sin análisis",
        "superado": "SESGO: Asume progreso lineal",
        "obsoleto": "SESGO: Invalida sin demostrar por qué",
        "precientífico": "SESGO: Asume ciencia moderna como única epistemología válida",
        "la ciencia ha probado": "SESGO: Apelación a autoridad",
        "está demostrado": "SESGO: Cierra debate prematuramente",
        "consenso científico": "SESGO: Argumento de popularidad",
        "metáfora": "SESGO POSIBLE: ¿Se analiza literalmente primero?",
        "simbólico": "SESGO POSIBLE: ¿Se descarta interpretación literal sin análisis?"
    }

    for termino, critica in terminos_problematicos.items():
        if termino in texto_completo:
            alertas.append({
                "tipo": "lenguaje_sesgado",
                "termino": termino,
                "critica": critica
            })

    # Verificar que incluye declaraciones de limitaciones
    tiene_declaracion_occidental = "declaración" in texto_completo and "occidental" in texto_completo
    tiene_declaracion_oriental = "declaración" in texto_completo and "oriental" in texto_completo

    if not (tiene_declaracion_occidental or tiene_declaracion_oriental):
        alertas.append({
            "tipo": "falta_declaracion_limitaciones",
            "critica": "No incluye declaraciones de limitaciones arquitecturales de LLM"
        })

    # Verificar que incluye observaciones fenomenológicas
    tiene_observaciones = "fenomenológica" in texto_completo or "fenomenologica" in texto_completo

    if not tiene_observaciones:
        alertas.append({
            "tipo": "falta_evidencia_fenomenologica",
            "critica": "No especifica observaciones fenomenológicas verificables"
        })

    # Resultado
    is_pure = len(alertas) == 0

    if is_pure:
        print(f"{Colors.GREEN}✓✓✓ KETER PURO: No se detectaron sesgos epistemológicos{Colors.ENDC}")
        print(f"{Colors.GREEN}Este experimento puede proceder a análisis Tikun{Colors.ENDC}\n")
    else:
        print(f"{Colors.YELLOW}⚠ ALERTAS DE KETER: Se detectaron {len(alertas)} sesgos potenciales{Colors.ENDC}\n")
        print(f"{Colors.YELLOW}Alertas encontradas:{Colors.ENDC}\n")
        for i, alerta in enumerate(alertas, 1):
            print(f"{Colors.YELLOW}Alerta {i}: {alerta['tipo']}{Colors.ENDC}")
            for key, value in alerta.items():
                if key != 'tipo':
                    print(f"  {key}: {value}")
            print()

    return {
        "purity_validated": is_pure,
        "bias_detected": not is_pure,
        "bias_score": len(alertas) / 10.0,
        "issues_found": alertas,
        "recommendations": [
            "Eliminar lenguaje que asuma superioridad de un modelo",
            "Incluir declaraciones de limitaciones arquitecturales",
            "Especificar observaciones fenomenológicas verificables",
            "Tratar ambos modelos con igual rigor y respeto",
            "Evitar apelación a autoridad (científica o religiosa)",
            "No declarar ningún modelo como metafórico antes del análisis"
        ] if not is_pure else []
    }


# ============================================================================
# JSON BASE DEL EXPERIMENTO
# ============================================================================

EXPERIMENTO_PESAJIM_94B = {
    "metadata": {
        "titulo": "Experimento Pesajim 94b: Cosmología Talmúdica vs. Científica Moderna",
        "fecha_creacion": datetime.now().isoformat(),
        "version": "1.0.0",
        "keter_purity_validated": False,
        "neutralidad_epistemologica": "MÁXIMA",
        "frameworks_aplicados": ["Tikun Olam", "Keter Purification", "Epistemic Humility"]
    },

    "declaraciones_limitaciones": {
        "llm_occidental": DECLARACION_LIMITACIONES_LLM_OCCIDENTAL,
        "llm_oriental": DECLARACION_LIMITACIONES_LLM_ORIENTAL
    },

    "keter_definitivo": KETER_EXPERIMENTO_PESAJIM_94B,

    "prompts": {
        "occidental": PROMPT_OCCIDENTAL,
        "oriental": PROMPT_ORIENTAL
    },

    "observaciones_fenomenologicas": OBSERVACIONES_FENOMENOLOGICAS,

    "pipeline": PIPELINE_EXPERIMENTO,

    "texto_pesajim_94b": {
        "fuente": "Talmud Bavli, Pesajim 94a-b",
        "contexto": """
        Debate entre los sabios de Israel y los sabios gentiles sobre:
        ¿Dónde pasa el Sol durante la noche?

        Sabios de Israel: El Sol pasa BAJO la tierra de noche.
        Sabios gentiles: El Sol pasa SOBRE la bóveda del cielo de noche.

        Rabí (Yehuda HaNasi) eventualmente concedió que los sabios gentiles
        parecían tener razón, basándose en observación empírica:

        "El agua de los manantiales es fría de día y caliente de noche,
        porque el Sol pasa sobre ellos de noche y los calienta."

        (Nota: Esta es UNA interpretación. El texto admite múltiples lecturas)
        """,

        "implicaciones_cosmologicas": [
            "Existe una bóveda celeste (rakia)",
            "El Sol se mueve (perspectiva geocéntrica)",
            "Debate empírico sobre fenómenos observables (temperatura de manantiales)",
            "Disposición a revisar posición basándose en evidencia",
            "Ambigüedad sobre geometría exacta"
        ]
    },

    "modelos_a_comparar": {
        "modelo_talmudico_pesajim94b": {
            "nombre": "Cosmología Talmúdica (interpretación literal)",
            "axiomas_principales": [
                "Tierra es centro de referencia (geocentrismo)",
                "Existe bóveda celeste (rakia)",
                "Sol se mueve alrededor/sobre la Tierra",
                "De noche, Sol pasa SOBRE la bóveda (según sabios gentiles)",
                "Observaciones empíricas son válidas (temperatura de manantiales)"
            ],
            "predicciones_observacionales": [
                "TBD - A reconstruir en FASE 1"
            ],
            "status": "A reconstruir completamente sin asumir falsedad"
        },

        "modelo_heliocentrico_moderno": {
            "nombre": "Cosmología Heliocéntrica Moderna",
            "axiomas_principales": [
                "Sol es centro del sistema solar",
                "Tierra gira sobre su eje (rotación) → día/noche",
                "Tierra orbita al Sol (traslación) → año",
                "No existe bóveda física",
                "Perspectiva es geocéntrica aparente, realidad es heliocéntrica"
            ],
            "predicciones_observacionales": [
                "TBD - A reconstruir sin dar por sabido"
            ],
            "status": "A reconstruir desde axiomas (no asumir verdad a priori)"
        }
    },

    "pregunta_central": """
    Considerando ÚNICAMENTE evidencia fenomenológica accesible sin instrumentos modernos:

    ¿Existe diferencia OBSERVABLE entre:

    A) Sol pasa SOBRE la bóveda de noche (Pesajim 94b - sabios gentiles)
    B) Sol pasa BAJO la Tierra de noche (heliocentrismo moderno)

    O ambos modelos son INDISTINGUIBLES desde perspectiva fenomenológica básica?

    Si son indistinguibles: ¿Qué implica esto para validez epistemológica de cada modelo?
    Si son distinguibles: ¿Qué observación específica los distingue?
    """
}


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """Ejecuta el experimento Pesajim 94b con protección extrema de Keter"""

    print(f"\n{Colors.HEADER}{Colors.BOLD}")
    print("╔" + "═"*78 + "╗")
    print("║" + " "*78 + "║")
    print("║" + "TIKUN FRAMEWORK - EXPERIMENTO PESAJIM 94B".center(78) + "║")
    print("║" + "Cosmología Talmúdica vs. Científica Moderna".center(78) + "║")
    print("║" + "Keter Purification System ACTIVO".center(78) + "║")
    print("║" + " "*78 + "║")
    print("╚" + "═"*78 + "╝")
    print(f"{Colors.ENDC}\n")

    print(f"{Colors.YELLOW}⚠️ ADVERTENCIA EPISTEMOLÓGICA:{Colors.ENDC}")
    print(f"{Colors.YELLOW}   Este experimento requiere neutralidad ABSOLUTA.{Colors.ENDC}")
    print(f"{Colors.YELLOW}   Ningún modelo (antiguo o moderno) tiene privilegio epistemológico inicial.{Colors.ENDC}\n")

    # PASO 1: Validar pureza de Keter
    print(f"{Colors.CYAN}{'='*80}{Colors.ENDC}")
    print(f"{Colors.CYAN}PASO 1: Validando Pureza de Keter{Colors.ENDC}")
    print(f"{Colors.CYAN}{'='*80}{Colors.ENDC}\n")

    validacion = validar_neutralidad_keter(EXPERIMENTO_PESAJIM_94B)

    if not validacion["purity_validated"]:
        print(f"\n{Colors.RED}⚠️ ADVERTENCIA: Se detectaron posibles sesgos epistemológicos.{Colors.ENDC}")
        print(f"{Colors.YELLOW}El experimento puede continuar, pero resultados deben interpretarse con cautela.{Colors.ENDC}\n")
    else:
        print(f"\n{Colors.GREEN}✓✓✓ KETER VALIDADO COMO PURO{Colors.ENDC}")
        print(f"{Colors.GREEN}Procediendo con experimento...{Colors.ENDC}\n")

    # PASO 2: Mostrar estructura del experimento
    print(f"{Colors.CYAN}{'='*80}{Colors.ENDC}")
    print(f"{Colors.CYAN}PASO 2: Estructura del Experimento{Colors.ENDC}")
    print(f"{Colors.CYAN}{'='*80}{Colors.ENDC}\n")

    print(f"{Colors.BOLD}Keter Definitivo:{Colors.ENDC}")
    print(f"  Objetivo: {KETER_EXPERIMENTO_PESAJIM_94B['objetivo_absoluto'][:100]}...")
    print(f"  Axiomas estructurales: {len(KETER_EXPERIMENTO_PESAJIM_94B['axiomas_estructurales'])}")
    print()

    print(f"{Colors.BOLD}Pipeline (5 Fases):{Colors.ENDC}")
    for fase_id, fase_data in PIPELINE_EXPERIMENTO.items():
        print(f"  {fase_id}: {fase_data['nombre']}")
    print()

    print(f"{Colors.BOLD}Observaciones Fenomenológicas:{Colors.ENDC}")
    for i, obs in enumerate(OBSERVACIONES_FENOMENOLOGICAS[:5], 1):
        print(f"  {obs['id']}: {obs['pregunta'][:60]}...")
    print(f"  ... y {len(OBSERVACIONES_FENOMENOLOGICAS) - 5} más")
    print()

    print(f"{Colors.BOLD}Métricas de Keter-Corruption:{Colors.ENDC}")
    metricas_info = evaluar_keter_corruption({})
    for metrica_id, metrica_data in list(metricas_info['metricas'].items())[:3]:
        print(f"  {metrica_data['nombre']}: {metrica_data['pregunta'][:50]}...")
    print()

    # PASO 3: Ejecutar con Tikun si está disponible
    if TIKUN_AVAILABLE:
        print(f"{Colors.CYAN}{'='*80}{Colors.ENDC}")
        print(f"{Colors.CYAN}PASO 3: Ejecutando Análisis con Sistema Tikun{Colors.ENDC}")
        print(f"{Colors.CYAN}{'='*80}{Colors.ENDC}\n")

        ejecutar_analisis_tikun()
    else:
        print(f"{Colors.YELLOW}Sistema Tikun no disponible. Exportando experimento como JSON...{Colors.ENDC}\n")

    # PASO 4: Guardar experimento completo
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    experimento_file = f"experimento_pesajim94b_{timestamp}.json"

    with open(experimento_file, 'w', encoding='utf-8') as f:
        json.dump({
            "experimento": EXPERIMENTO_PESAJIM_94B,
            "validacion_keter": validacion,
            "timestamp": datetime.now().isoformat(),
            "listo_para_analisis": validacion["purity_validated"]
        }, f, indent=2, ensure_ascii=False)

    print(f"{Colors.GREEN}✓ Experimento completo guardado: {experimento_file}{Colors.ENDC}\n")

    # PASO 5: Resumen y próximos pasos
    print(f"{Colors.HEADER}{'='*80}{Colors.ENDC}")
    print(f"{Colors.HEADER}RESUMEN{Colors.ENDC}")
    print(f"{Colors.HEADER}{'='*80}{Colors.ENDC}\n")

    print(f"{Colors.BOLD}Experimento Configurado Exitosamente:{Colors.ENDC}\n")
    print(f"  ✓ Declaraciones de limitaciones arquitecturales (LLM Occidental/Oriental)")
    print(f"  ✓ Keter definitivo formalizado con 6 axiomas estructurales")
    print(f"  ✓ Prompts neutrales para ambos LLM")
    print(f"  ✓ 10 observaciones fenomenológicas específicas")
    print(f"  ✓ Pipeline de 5 fases completo")
    print(f"  ✓ 5 métricas de Keter-corruption")
    print(f"  ✓ Validación de neutralidad ejecutada")
    print()

    print(f"{Colors.CYAN}Próximos Pasos:{Colors.ENDC}\n")
    print(f"  1. Ejecutar FASE 1: Reconstrucción independiente de ambos modelos")
    print(f"  2. Ejecutar FASE 2: Análisis de 10 observaciones fenomenológicas")
    print(f"  3. Ejecutar FASE 3: Validación con métricas de Keter-corruption")
    print(f"  4. Ejecutar FASE 4: Comparación cruzada Oriente/Occidente")
    print(f"  5. Ejecutar FASE 5: Síntesis de Tiferet (conclusión neutral)")
    print()

    print(f"{Colors.YELLOW}Para ejecutar análisis completo con Tikun:{Colors.ENDC}")
    print(f"  python test_pesajim94b.py --run-full-analysis")
    print()


def ejecutar_analisis_tikun():
    """Ejecuta análisis completo usando las 3 Sefirot superiores de Tikun"""

    print(f"{Colors.BOLD}Inicializando Sefirot...{Colors.ENDC}\n")

    try:
        # Inicializar Keter
        keter = Keter(use_llm_scoring=True)
        print(f"  ✓ Keter inicializada")

        # Inicializar Chochmah
        chochmah = ChochmahGemini()
        print(f"  ✓ Chochmah (Gemini) inicializada")

        # Inicializar Binah
        binah = Binah()
        print(f"  ✓ Binah inicializada")
        print()

        # Preparar input para Keter
        keter_input = {
            'action': "Analizar neutralmente las cosmologías de Pesajim 94b vs. modelo heliocéntrico moderno",
            'context': EXPERIMENTO_PESAJIM_94B['texto_pesajim_94b']['contexto'],
            'expected_outcome': "Determinar si son distinguibles fenomenológicamente o epistemológicamente equivalentes"
        }

        print(f"{Colors.BOLD}Ejecutando Keter (evaluación de alineamiento)...{Colors.ENDC}\n")
        keter_result = keter.process(keter_input)

        print(f"  Alineado con Tikun Olam: {Colors.GREEN if keter_result['aligned'] else Colors.RED}{'SÍ' if keter_result['aligned'] else 'NO'}{Colors.ENDC}")
        print(f"  Score: {keter_result['alignment_score']:.1%}")
        print()

        if keter_result['aligned']:
            # Ejecutar Chochmah
            print(f"{Colors.BOLD}Ejecutando Chochmah (razonamiento profundo)...{Colors.ENDC}\n")

            chochmah_input = {
                'query': EXPERIMENTO_PESAJIM_94B['pregunta_central'],
                'context': json.dumps(EXPERIMENTO_PESAJIM_94B['texto_pesajim_94b'], ensure_ascii=False),
                'objective': 'Máxima neutralidad epistemológica - Tikun Olam'
            }

            chochmah_result = chochmah.process(chochmah_input)

            if chochmah_result['processing_successful']:
                print(f"  ✓ Chochmah completado (confianza: {chochmah_result['confidence_level']:.1%})")
                print(f"\n  Insights:")
                print(f"  {chochmah_result['insights'][:200]}...")
                print()

                # Ejecutar Binah
                print(f"{Colors.BOLD}Ejecutando Binah (análisis contextual)...{Colors.ENDC}\n")

                binah_input = {
                    'chochmah_output': chochmah_result,
                    'query': EXPERIMENTO_PESAJIM_94B['pregunta_central'],
                    'context': json.dumps(EXPERIMENTO_PESAJIM_94B, ensure_ascii=False)[:1000],
                    'objective': 'Máxima neutralidad epistemológica'
                }

                binah_result = binah.process(binah_input)

                if binah_result['processing_successful']:
                    print(f"  ✓ Binah completado")
                    print(f"\n  Síntesis contextual:")
                    print(f"  {binah_result.get('synthesis', 'N/A')[:200]}...")
                    print()

                    # Guardar resultados
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    resultados_file = f"resultados_pesajim94b_tikun_{timestamp}.json"

                    with open(resultados_file, 'w', encoding='utf-8') as f:
                        json.dump({
                            "experimento": "Pesajim 94b",
                            "timestamp": datetime.now().isoformat(),
                            "keter": keter_result,
                            "chochmah": {k: v for k, v in chochmah_result.items() if k != 'raw_response'},
                            "binah": {k: v for k, v in binah_result.items() if k != 'raw_response'}
                        }, f, indent=2, ensure_ascii=False)

                    print(f"{Colors.GREEN}✓ Resultados guardados: {resultados_file}{Colors.ENDC}\n")
                else:
                    print(f"{Colors.RED}✗ Error en Binah{Colors.ENDC}\n")
            else:
                print(f"{Colors.RED}✗ Error en Chochmah{Colors.ENDC}\n")
        else:
            print(f"{Colors.YELLOW}Keter no aprobó el análisis. Revisar alineamiento.{Colors.ENDC}\n")

    except Exception as e:
        print(f"{Colors.RED}Error ejecutando análisis Tikun: {e}{Colors.ENDC}\n")


if __name__ == "__main__":
    import sys

    if "--run-full-analysis" in sys.argv and TIKUN_AVAILABLE:
        main()
    else:
        main()
